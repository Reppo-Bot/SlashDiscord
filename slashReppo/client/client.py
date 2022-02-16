""" This module is resposnible for holding the client for the library"""
from typing import OrderedDict, Any
from ..command.command import Command
import json
import asyncio
import websockets
import requests
from ..util.gateway import GATEWAY_OPCODES

BASE_URL = 'https://discord.com/api/v9'
API_VERSION = "/?v=9&encoding=json"

class Client:
    commands: list
    command_cache: OrderedDict[str, Any]
    event_cache: OrderedDict[str, Any]
    client_events: OrderedDict[str, Any]
    _token: str
    _app_id: str
    heartbeat_interval: int # miliseconds
    initial_heartbeat: int # heartbeat * rand(0->1)
    websocket: Any
    intents: int
    def __init__(self, token, intents, app_id, commands=[]) -> None:
        self._token     = token
        self.intents    = intents
        self._app_id    = app_id
        self.commands   = commands
    def __call__(self, *args: Any, **kwds: Any) -> Any: ...
    def push(self, command) -> None:
        self.command_cache[command.name] = command.handler
        self.commands.push(command)
    def push(self, commands) -> None:
        for command in commands:
            self.push(command)
    def on(self, event, callback) -> None:
        self.event_cache[event] = callback
    def connect(self) -> bool:
        payload = requests.get(BASE_URL + "/gateway/bot", headers={"Authorization": "Bot " + self._token})
        res = payload.json()
        print(res)
        websocketUrl = res["url"] + API_VERSION
        asyncio.run(self._startup(websocketUrl))
    def disconnect() -> bool: ...
    def register(self) -> bool:
        for command in self.commmands:
            try:
                if (command.json() == None):
                    raise f"Invalid command {command.str()}"
            except Exception(e):
                print(e)
                return False
        header = {"Authorization": f"Bot {self._token}"}
        registered = []
        try:
            for command in self.commands:
                for id in command.guild_ids:
                    url = f"https://discord.com/api/v8/applications/{self.app_id}/guilds/{id}/commands"
                    r = requests.post(url, headers=header, json=command.json())
                    registered.append(f"{url}/{r.command_id}")
            print("Successfully registered all commands")
        except Exception(e):
            print("Failed to regeister some commands, attempting to deregister posted ones...")
            for url in registered:
                r = requests.delete(url)
                if(r.status != 200):
                    print(f"Faield to deregister {url}")
            print("Successfully deregistered partial command set")
    async def _startup(self, websocketUrl) -> bool:
        self.websocket = await websockets.connect(websocketUrl, ping_interval=None)
        helloResponse = json.loads(await self.websocket.recv())
        print(helloResponse)
        if(helloResponse["op"] != GATEWAY_OPCODES.HELLO.value):
            print("Error: Unexpected init opcode")
            return False
        self.heartbeat_interval = helloResponse["d"]["heartbeat_interval"]
        response = {
            "op": 2,
            "d": {
                "token": self._token,
                "intents": 513,
                "properties": {
                    "$os": "linux",
                    "$browser": "slash-reppo",
                    "$device": "slash-reppo"
                }
            }
        }
        await self.websocket.send(json.dumps(response))
        await asyncio.gather(self._loop(), self._heartbeatLoop(),)
    async def _loop(self) -> None:
        async for message in self.websocket:
            print(message)
    async def _heartbeatLoop(self) -> None:
        heartbeat = {
            "op": 1,
            "d": None
        }
        heartbeat = json.dumps(heartbeat)
        heartbeatTime = self.heartbeat_interval * .0001
        await self.websocket.send(heartbeat)
        asyncio.sleep(heartbeatTime * .7)
        while True:
            print("Beating", heartbeatTime)
            await self.websocket.send(heartbeat)
            await asyncio.sleep(heartbeatTime)

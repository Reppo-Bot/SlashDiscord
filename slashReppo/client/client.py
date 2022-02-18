""" This module is resposnible for holding the client for the library"""
from typing import OrderedDict, Any
from ..command.command import Command
import json
import asyncio
import websockets
import requests
from ..util.gateway import GATEWAY_OPCODES, Payload

BASE_URL = 'https://discord.com/api/v9'
API_VERSION = "/?v=9&encoding=json"

class Client:
    def __init__(self, token, intents, app_id, commands=[]):
        self._token     = token
        self.intents    = intents
        self._app_id    = app_id
        self.commands   = commands
        self.command_cache = OrderedDict()
        self.event_cache = OrderedDict()

    def __call__(self, *args, **kwds): ... # todo

    def push(self, command):
        self.command_cache[command.name] = command.handler
        self.commands.push(command)

    def push(self, commands):
        for command in commands:
            self.push(command)

    def on(self, event, callback):
        self.event_cache[event] = callback

    def connect(self):
        payload = requests.get(BASE_URL + "/gateway/bot", headers={"Authorization": "Bot " + self._token})
        res = payload.json()
        print(res)
        websocketUrl = res["url"] + API_VERSION
        asyncio.run(self._startup(websocketUrl))

    def disconnect(): ... # todo

    def register(self):
        for command in self.commmands:
            try:
                if (command.json() == None):
                    raise f"Invalid command {command.str()}"
            except Exception as e:
                print(e)
                return False
        header = {"Authorization": f"Bot {self._token}"}
        registered = []
        try:
            for command in self.commands:
                for id in command.guild_ids:
                    url = f"https://discord.com/api/v9/applications/{self.app_id}/guilds/{id}/commands"
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

    async def _startup(self, websocketUrl):
        self.websocket = await websockets.connect(websocketUrl, ping_interval=None)
        helloResponse = Payload(await self.websocket.recv())
        print(helloResponse)

        if(helloResponse.op != GATEWAY_OPCODES.HELLO.value):
            print("Error: Unexpected init opcode")
            return False
        self.heartbeat_interval = helloResponse.d["heartbeat_interval"]
        response = {
            "op": 2,
            "d": {
                "token": self._token,
                "intents": self.intents,
                "properties": {
                    "$os": "linux",
                    "$browser": "slash-reppo",
                    "$device": "slash-reppo"
                }
            }
        }
        await self.websocket.send(json.dumps(response))
        await asyncio.gather(self._loop(), self._heartbeatLoop(),)

    async def _loop(self):
        async for message in self.websocket:
            payload = Payload(message)
            print(payload)

    async def _heartbeatLoop(self):
        heartbeat = {
            "op": 1,
            "d": None
        }
        heartbeat = json.dumps(heartbeat)
        heartbeatTime = self.heartbeat_interval * .0001
        await self.websocket.send(heartbeat)
        await asyncio.sleep(heartbeatTime * .7)
        while True:
            print("Beating", heartbeatTime)
            await self.websocket.send(heartbeat)
            await asyncio.sleep(heartbeatTime)

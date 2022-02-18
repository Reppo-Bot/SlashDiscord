""" This module is resposnible for holding the client for the library"""
from typing import OrderedDict, Any
from ..command.command import Command
import json
import asyncio
import websockets
import requests
from ..util.gateway import GATEWAY_OPCODES, GATEWAY_CLOSE_CODES, Payload
import platform

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
        self.heartbeat = Payload({"op": 1,"d": None})
        self._reconnect = False
        self._die = False
        self._can_resume = False
    def __call__(self, *args, **kwds): ... # todo

    def push(self, c):
        if not c:
            raise Exception("Invalid command")

        if(type(c) is list):
            for command in c:
                self.commands.append(command)
                self.command_cache[command.name] = command.handler
        else:
            self.command_cache[c.name] = c.handler
            self.commands.append(c)

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
        while True:
            print()
            print("Restarted Bot")
            print()
            self.websocket = await websockets.connect(websocketUrl, ping_interval=None)
            helloResponse = Payload(await self.websocket.recv())
            print(helloResponse)
            if(helloResponse.op != GATEWAY_OPCODES.HELLO.value):
                print("Error: Unexpected init opcode")
                return False
            self.heartbeat_interval = helloResponse.d["heartbeat_interval"]
            if(self._can_resume):
                self._can_resume = False
                resume = Payload({
                    "op": 6,
                    "d": {
                        "token": self._token,
                        "session_id": self.session_id,
                        "seq": self._last_sequence
                    }
                })
                await self.websocket.send(str(resume))
            else:
                response = Payload({
                    "op": 2,
                    "d": {
                        "token": self._token,
                        "intents": self.intents,
                        "properties": {
                            "$os": platform.system(),
                            "$browser": "slash-reppo",
                            "$device": "slash-reppo"
                        }
                    }
                })
                await self.websocket.send(str(response))
                ready = Payload(await self.websocket.recv())
                if(ready.t != "READY"):
                    print("Failed to receive READY")
                    return
                print(ready)
                self._heartbeat_heard = True
                self.session_id = ready.d["session_id"]
                self._last_sequence = ready.s

            done, pending = await asyncio.wait(
                [self._loop(), self._heartbeatLoop()],
                return_when=asyncio.FIRST_COMPLETED)
            for task in pending:
                task.cancel()
            if(self._can_resume):
                print()
                print("Attempting to resume")
                print()
                await self.websocket.close(code=4099, reason="Attempting Resume")
                continue

            await self.websocket.close()
            if(self._die):
                break

            await asyncio.sleep(5)
        print("Exiting")

    async def _loop(self):
        async for message in self.websocket:
            _payload = Payload(message)
            print(_payload)
            if(_payload.s != None):
                self._last_sequence = _payload.s
            if(_payload.op == GATEWAY_OPCODES.HEARTBEAT_ACK.value):
                self._heartbeat_heard = True
                continue
            if(_payload.op in [GATEWAY_OPCODES.INVALID_SESSION.value,
                                GATEWAY_CLOSE_CODES.UNKNOWN_ERROR.value,
                                GATEWAY_CLOSE_CODES.UNKNOWN_OPCODE.value,
                                GATEWAY_CLOSE_CODES.DECODE_ERROR.value,
                                GATEWAY_CLOSE_CODES.NOT_AUTHENTICATED.value,
                                GATEWAY_CLOSE_CODES.ALREADY_AUTHENTICATED.value,
                                GATEWAY_CLOSE_CODES.RATE_LIMITED.value,
                                GATEWAY_CLOSE_CODES.INVALID_SEQ.value,
                                GATEWAY_CLOSE_CODES.SESSION_TIMED_OUT.value]):
                print(f"Error: {GATEWAY_CLOSE_CODES(_payload.op)}")
                print("Trying to Reconnect")
                return
            if(_payload.op in [GATEWAY_CLOSE_CODES.AUTHENTICATION_FAILED.value,
                            GATEWAY_CLOSE_CODES.INVALID_SHARD.value,
                            GATEWAY_CLOSE_CODES.SHARDING_REQUIRED.value,
                            GATEWAY_CLOSE_CODES.INVALID_API_VERSION.value,
                            GATEWAY_CLOSE_CODES.INVALID_INTENTS.value,
                            GATEWAY_CLOSE_CODES.DISALLOWED_INTENTS.value]):
                self._die = True
                print(f"Error: {GATEWAY_OPCODES(_payload.op)}")
                print("Cannot Reconnect. Starting shutdown")
                return
            if(_payload.op == GATEWAY_OPCODES.HEARTBEAT.value):
                print("Beat Requested! Beating")
                await self.websocket.send(str(self.heartbeat))
                continue

    async def _heartbeatLoop(self):
        heartbeatTime = self.heartbeat_interval * .0001
        await self.websocket.send(str(self.heartbeat))
        self._heartbeat_heard = False
        print("Beating at", heartbeatTime)
        await asyncio.sleep(heartbeatTime * .7)
        while self._heartbeat_heard:
            print("Beating")
            await self.websocket.send(str(self.heartbeat))
            self._heartbeat_heard = False
            await asyncio.sleep(heartbeatTime)
        print("Disconnect detected, trying to reconnect...")
        self._can_resume = True

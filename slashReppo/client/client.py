""" This module is resposnible for holding the client for the library"""
from typing import OrderedDict, Any
from ..command.command import Command
import json
import asyncio
import websockets
import requests
from ..util.gateway import GATEWAY_OPCODES, GATEWAY_CLOSE_CODES, Payload
import platform
import logging

BASE_URL = 'https://discord.com/api/v9'
API_VERSION = "/?v=9&encoding=json"

class Client:
    def __init__(self, token, intents, app_id, commands=[], log_level=0, log_file="slashReppo.log"):
        self._token         = token
        self.intents        = intents
        self._app_id        = app_id
        self.commands       = commands
        self.command_cache  = OrderedDict()
        self.event_cache    = OrderedDict()
        self.heartbeat      = Payload({"op": 1,"d": None})
        self._reconnect     = False
        self._die           = False
        self._can_resume    = False
        logging.basicConfig(filename=log_file, encoding='utf-8', level=log_level)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
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
        self.logger.debug(res)
        websocketUrl = res["url"] + API_VERSION
        asyncio.run(self._startup(websocketUrl))

    def disconnect(): ... # todo

    def register(self):
        for command in self.commmands:
            try:
                if (command.json() == None):
                    raise f"Invalid command {command.str()}"
            except Exception as e:
                self.logger.error(e)
                return False
        header = {"Authorization": f"Bot {self._token}"}
        registered = []
        try:
            for command in self.commands:
                for id in command.guild_ids:
                    url = f"https://discord.com/api/v9/applications/{self.app_id}/guilds/{id}/commands"
                    self.logger.debug(f"Registering: {url}")
                    r = requests.post(url, headers=header, json=command.json())
                    registered.append(f"{url}/{r.command_id}")
            print("Successfully registered all commands")
            self.logger.info("Registered all commands")
        except Exception(e):
            print("Failed to regeister some commands, attempting to deregister posted ones...")
            self.logger.error(e)
            self.logger.error("Command registration failed")
            for url in registered:
                r = requests.delete(url)
                if(r.status != 200):
                    print(f"Faield to deregister {url}")
                    self.logger.error(f"Failed to deregister {url}")
            print("Successfully deregistered partial command set")
            self.logger.info("Deregistered partial command set")

    async def _startup(self, websocketUrl):
        while True:
            self.websocket = await websockets.connect(websocketUrl, ping_interval=None)
            helloResponse = Payload(await self.websocket.recv())
            self.logger.debug(helloResponse)
            if(helloResponse.op != GATEWAY_OPCODES.HELLO.value):
                print("Error: Unexpected init opcode")
                self.logger.error("Unexpected init opcode")
                return False
            self.heartbeat_interval = helloResponse.d["heartbeat_interval"]
            self.logger.debug(f"HEARTBEAT: {self.heartbeat_interval}")
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
                self.logger.debug(f'Attempting to resume with payload: {resume}')
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
                self.logger.debug(f'Attempting to connect with payload: {response}')
                await self.websocket.send(str(response))
                ready = Payload(await self.websocket.recv())
                if(ready.t != "READY"):
                    print("Failed to receive READY")
                    self.logger.error("Failed to get READY from discord")
                    self.logger.error(f"Received payload: {ready}")
                    return
                self.logger.debug(ready)
                self._heartbeat_heard = True
                self.session_id = ready.d["session_id"]
                self._last_sequence = ready.s

            print("Successfully connected to discord!")
            done, pending = await asyncio.wait(
                [self._loop(), self._heartbeatLoop()],
                return_when=asyncio.FIRST_COMPLETED)
            for task in pending:
                task.cancel()
            if(self._can_resume):
                self.logger.waring("Attempting to resume")
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
                self.logger.error(f"Bad opcode: {GATEWAY_CLOSE_CODES(_payload.op)}")
                self.logger.error("Attempting to reconnect")
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
                self.logger.error(f"Bad opcode: {GATEWAY_CLOSE_CODES(_payload.op)}")
                self.logger.error("Shutdown")
                return
            if(_payload.op == GATEWAY_OPCODES.HEARTBEAT.value):
                self.logger.warning(f"Heartbeat requested!")
                await self.websocket.send(str(self.heartbeat))
                continue

    async def _heartbeatLoop(self):
        heartbeatTime = self.heartbeat_interval * .0001
        await self.websocket.send(str(self.heartbeat))
        self._heartbeat_heard = False
        self.logger.debug(f"Beating at {heartbeatTime}")
        await asyncio.sleep(heartbeatTime * .7)
        while self._heartbeat_heard:
            await self.websocket.send(str(self.heartbeat))
            self._heartbeat_heard = False
            await asyncio.sleep(heartbeatTime)
        self.logger.error("Detected disconnect. Trying reconnect")
        print("Disconnect detected, trying to reconnect...")
        self._can_resume = True

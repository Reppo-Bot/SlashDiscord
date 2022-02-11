""" This module is resposnible for holding the client for the library"""
from typing import OrderedDict, Any
from .command import Command
import json

class Client:
    commands: list(Command)
    command_cache: OrderedDict[str, Any]
    event_cache: OrderedDict[str, Any]
    client_events: OrderedDict[str, Any]
    _token: str
    _app_id: str
    heartbeat_interval: int # miliseconds
    initial_heartbeat: int # heartbeat * rand(0->1)
    def __init__(self, token, intents, _app_id) -> None: ...
    def __init__(self, token, intents, _app_id, commands) -> None: ...
    def __call__(self, *args: Any, **kwds: Any) -> Any: ...
    def push(self, command) -> None:
        self.command_cache[command.name] = command.handler
        self.commands.push(command)
    def push(self, commands) -> None:
        for command in commands:
            self.push(command)
    def on(self, event, callback) -> None:
        self.event_cache[event] = callback
    def connect() -> bool: ...
    def disconnect() -> bool: ...
    def register(self) -> bool:
        for command in self.commmands:
            try:
                if (command.json() == None) raise f"Invalid command {command.str()}"
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

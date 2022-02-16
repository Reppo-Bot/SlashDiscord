"""Interface for discord commands"""

from typing import Any, Callable
from enum import Enum
import json

option = dict
choice = dict

def create_option(name: str, desc: str, option_type: int, required: bool, choices: list = None) -> option: ...

class COMMAND_TYPE(Enum):
    """Enum for command types"""
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3

class Command:
    name: str
    _type: int
    description: str
    options: list = None
    guild_ids: list = None
    default_perms: bool = True
    permissions: dict = None
    handler: Callable[...,Any] = None
    def json(self) -> dict:
        _dict = {
            "name": self.name.lower(),
            "type": self._type,
            "default_permission": self.default_perms,
            "description": self.description
        }
        if (self.options != None and self.options.length() != 0):
            _dict["options"] = self.options
        if (self.permissions != None):
            _dict["permissions"] = self.permissions
        try:
            return json.loads(json.dumps(_dict))
        except:
            return None
    def __init__(self, name: str, description: str, options: list = None) -> None: ...
    def __call__(self, *args: Any, **kwds: Any) -> Any: ... # calls the handler function with the given args?

class SlashCommand(Command):
    _type: int = COMMAND_TYPE.CHAT_INPUT

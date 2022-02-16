"""Interface for discord commands"""

from typing import Any, Callable
from enum import Enum
import json

option = dict
choice = dict

class COMMAND_TYPE(Enum):
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3

def create_option(name, desc, option_type, required, choices=None): ... # todo

class Command:
    def __init__(self, name, type, description, options=None, guild_ids=None, default_perms=True, permissions=None, handler=None):
        self.name = name
        self._type = type
        self.description = description
        self.options = options
        self.guild_ids = guild_ids
        self.default_perms = default_perms
        self.permissions = permissions
        self.handler = handler

    def __call__(self, *args, **kwds): ... # todo??

    def json(self):
        _dict = {
            "name": self.name.lower(),
            "type": self._type,
            "default_permission": self.default_perms,
            "description": self.description,
            "options": self.options,
            "permissions": self.permissions
        }
        try:
            return json.loads(json.dumps(_dict))
        except:
            return None

class SlashCommand(Command):
    def __init__(self, name, description, options=None, guild_ids=None, default_perms=True, permissions=None, handler=None):
        super().__init__(name, description, options, guild_ids, default_perms, permissions, handler)
        self._type = COMMAND_TYPE.CHAT_INPUT.value
    
    def __iter__(self) -> dict:
        return self.json()
    
    

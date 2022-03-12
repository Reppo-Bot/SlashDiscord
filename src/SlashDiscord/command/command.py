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
        self.type = type
        self.description = description
        self.options = options
        self.guild_ids = guild_ids
        self.default_permission = default_perms
        self.permissions = permissions
        self.handler = handler

    def __repr__(self):
        return str(self.json())

    def json(self):
        return {
            "name" : self.name,
            "type": self.type,
            "guild_ids" : self.guild_ids,
            "description" : self.description,
            "options" : self.options,
            "default_permission" : self.default_permission
        }

class SlashCommand(Command):
    def __init__(self, name, description, options=None, guild_ids=None, default_perms=True, permissions=None, handler=None):
        super().__init__(name=name, description=description, options=options, guild_ids=guild_ids, default_perms=default_perms, permissions=permissions, handler=handler, type=COMMAND_TYPE.CHAT_INPUT.value)

    def __iter__(self) -> dict:
        yield "name", self.name.lower()
        yield "type", self.type
        yield "default_permission", self.default_perms
        yield "description", self.description
        yield "options", self.options
        yield "permissions", self.permissions

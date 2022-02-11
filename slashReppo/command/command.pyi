"""Interface for discord commands"""

from typing import Any, Callable
from enum import Enum

option = dict
choice = dict

def create_option(name: str, desc: str, option_type: int, required: bool, choices: list(str) = None) -> option: ...

class COMMAND_TYPE(Enum):
    """Enum for command types"""
    CHAT_INPUT = 1
    USER = 2
    MESSAGE = 3

class Command:
    name: str
    _type: int
    description: str
    options: list(option) = None
    guild_ids: list(int) = None
    default_perms: bool = True
    permissions: dict = None
    handler: Callable[...,Any] = None
    def __init__(self, name: str, description: str, options: list(option) = None) -> None: ...
    def __call__(self, *args: Any, **kwds: Any) -> Any: ... # calls the handler function with the given args?

class SlashCommand(Command):
    _type: int = COMMAND_TYPE.CHAT_INPUT

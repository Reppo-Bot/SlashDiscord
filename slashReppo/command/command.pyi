"""Interface for discord commands"""

from typing import Any, Callable
from enum import IntEnum

option = dict
choice = dict

"""Enum for command types"""
class COMMAND_TYPE(IntEnum): ...

def create_option(name: str, desc: str, option_type: int, required: bool, choices: list(str) = None) -> option: ...

class Command:
    name: str
    _type: int
    description: str
    options: list(option) = None
    guild_ids: list(int) = None
    default_permission: bool = True
    permissions: dict = None
    handler: Callable[...,Any] = None
    def __init__(self, name: str, type: int, description: str, options: list(option) = None) -> None: ...
    def __call__(self, *args: Any, **kwds: Any) -> Any: ... # calls the handler function with the given args?
    def json(self) -> dict: ...

class SlashCommand(Command):
    _type: int = COMMAND_TYPE.CHAT_INPUT.value
    def __init__(self, name: str, description: str, options: list(option)=None, guild_ids: list(str)=None, default_perms: bool=True, permissions: dict=None, handler: Callable=None): ...
    def __iter__(self) -> dict: ...

"""The interface for the client module"""
from typing import OrderedDict, Any
import asyncio

from slashReppo.command.command import Command

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
    _session_id: str
    _last_sequence: int
    _heartbeat_heard: bool
    _can_resume: bool
    _die: bool
    log_level: int
    def __init__(self, token, intents, app_id, commands=None) -> None: ...
    def __call__(self, *args: Any, **kwds: Any) -> Any: ...
    def push(self, c: Command | list(Command)) -> None: ...
    def on(self, event, callback) -> None: ...
    def connect(self) -> bool: ...
    def disconnect() -> bool: ...
    def register(self) -> bool: ...
    async def _startup(self, websocketUrl) -> bool: ...
    async def _loop(self) -> None: ...
    async def _heartbeatLoop(self) -> None: ...

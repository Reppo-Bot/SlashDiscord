"""The interface for the client module"""
from typing import OrderedDict, Any
import asyncio

from slashReppo.command.command import Command

class Client:
    """A client that can connect to discord.
    This class can start the connection with the API and websocket.
    """
    commands: OrderedDict[str, Any]
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
    def __init__(self, token, intents, app_id, commands=[], log_level=0, log_file="slashReppo.log") -> None: ...
    """Initialization of client class.

    :param token: discord bot token
    :type token: str
    :param intents: discord intents. 0 for slash commands
    :type intents: int
    :param app_id: discord application id
    :type app_id: int
    :param commands: list, or single command for the bot to map registerd commands to.
    :type commands: list(slashReppo.command) | slashReppo.command
    :param log_level: verboseness of logging, defaults to 0
    :type log_level: int, plugged directly into default python logger library.
    :param log_file: file to send logs to
    :type log_file: str

    .. notes:: initialization of the class will start the logger, and set basic config.
        Simply making an instance of client does not start any connections or send any
        requests
    """
    def push(self, c: Command | list(Command)) -> None: ...
    """Push commands to the client's list of commands.

    :param c: list, or single command for the bot to map registerd commands to.
    :type c: list(slashReppo.command) | slashReppo.command
    """
    def pushHandler(self, handler, handlerType) -> None: ...
    """Push handlers to the clients list of handlers

    :param handler: function called every time payload on websocket is of type handlerType
    :type handler: function
    :param handlerType: name of discord event sent over the websocket
    :type handlerType: string
    """
    def deleteMessage(self, channelId, messageId) -> None: ...
    """Delete message given a channel and message id
    :param channelId: id of the channel containing the message
    :type channelId: string
    :param messageId: id of the individual message in a given channel
    :param messageId: string
    """
    def getMessage(self, channelId, messageId) -> dict: ...
    """Get attributes and contents of a message
    :param channelId: id of the channel containing the message
    :type channelId: string
    :param messageId: id of the individual message in a given channel
    :param messageId: string
    """
    def createMessage(self, channelId, content) -> None: ...
    """Send a message to a given channel with simple contents
    :param channelId: id of the channel containing the message
    :type channelId: string
    :param content: string contents of the message
    :param content: string
    """
    def on(self, event, callback) -> None: ...
    def connect(self) -> None: ...
    """Initialize connection to the discord server.
    To close the connection, use ctrl+c to interupt the connection and close
    all async tasks.
    """
    def disconnect(self) -> None: ...
    """Trigger disconnect from the websocet and close all async tasks"""
    def register(self) -> bool: ...
    """Register all commands in Client's command list to discord

    :rtype: bool
    :return: if registration was successful
    """
    def deregister(self, guild_ids = []) -> bool: ...
    """Deregister all commands for each guild in list
    This commonly gets rate limited, so it might take a few seconds.

    :rtype: bool
    :return: if deregistration was successful
    """
    async def _startup(self, websocketUrl) -> bool: ...
    async def _loop(self) -> None: ...
    async def _heartbeatLoop(self) -> None: ...

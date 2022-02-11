"""Interaction class for responses to commands"""

from slashReppo.util.user import Member

class Interaction:
    _type: int = None
    member: Member = None
    id: str = None
    guild_id: str = None
    channel_id: str = None
    data: dict = None
    def __init__(self, type: int, member: Member, id: str, guild_id: str = None, channel_id: str = None, data: dict = None) -> None: ...
    def send(socket, data) -> None: ...
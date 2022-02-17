"""User data from response"""

class User:
    id: str=None
    username: str=None
    avatar: str=None
    discriminator: str=None
    public_flags: int=None
    def __init__(self, id: str=None, username: str=None, avatar: str=None, discriminator: str=None, public_flags: int=None) -> None: ...
    def __iter__(self) -> dict: ...

class Member:
    user: User=None
    roles: list(str)=None
    premium_since: str=None
    permissions: str=None
    pending: bool=False
    nick: str=None
    mute: bool=False
    joined_at: str=None
    is_pending: bool=False
    deaf: bool=False
    def __init__(self, user: User=None, roles: list(str)=None, premium_since: str=None, permissions: str=None, pending: bool=False, nick: str=None, mute: bool=False, joined_at: str=None, is_pending: bool=False, deaf: bool=False) -> None: ...
    def __iter__(self) -> dict: ...
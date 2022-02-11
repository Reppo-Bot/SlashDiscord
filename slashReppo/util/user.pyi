"""User data from response"""

class User:
    id: str = None
    username: str = None
    avatar: str = None
    discriminator: str = None
    public_flags: int = None

class Member:
    user: User = None
    roles: list(str) = None
    premium_since: str = None
    permissions: str = None
    pending: bool = False
    nick: str = None
    mute: bool = False
    joined_at: str = None
    is_pending: bool = False
    deaf: bool = False
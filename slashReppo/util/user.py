class User:
    def __init__(self, id = None, username = None, avatar = None, discriminator = None, public_flags = None):
        self.id = id
        self.username = username
        self.avatar = avatar
        self.discriminator = discriminator
        self.public_flags = public_flags
    def __iter__(self):
        return {
            "id": self.id,
            "username": self.username,
            "avatar": self.avatar,
            "discriminator": self.discriminator,
            "public_flags": self.public_flags
        }

class Member:
    def __init__(self, user = None, roles = None, premium_since = None, permissions = None, pending = False, nick = None, mute = False, joined_at = None, is_pending = False, deaf = False):
        self.user = user
        self.roles = roles
        self.premium_since = premium_since
        self.permissions = permissions
        self.pending = pending
        self.nick = nick
        self.mute = mute
        self.joined_at = joined_at
        self.is_pending = is_pending
        self.deaf = deaf
    def __iter__(self) -> dict:
        return {
            "user": self.user,
            "roles": self.roles,
            "premium_since": self.premium_since,
            "permissions": self.permissions,
            "pending": self.pending,
            "nick": self.nick,
            "mute": self.mute,
            "joined_at": self.joined_at,
            "is_pending": self.is_pending,
            "deaf": self.deaf
        }
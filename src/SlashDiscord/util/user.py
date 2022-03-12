class User:
    def __init__(self, user):
        _user = json.loads(user) if type(user) is str else user
        self.id = _user['id']
        self.username = _user['username']
        self.avatar = _user['avatar']
        self.discriminator = _user['discriminator']
        self.public_flags = _user['public_flags']
    def __iter__(self):
        return {
            "id": self.id,
            "username": self.username,
            "avatar": self.avatar,
            "discriminator": self.discriminator,
            "public_flags": self.public_flags
        }

class Member:
    def __init__(self, member):
        _member = json.loads(member) if type(member) is str else member
        self.user = User(member['user'])
        self.roles = _member['roles']
        self.premium_since = _member['premium_since']
        self.permissions = _member['permissions']
        self.pending = _member['pending']
        self.nick = _member['nick']
        self.mute = _member['mute']
        self.joined_at = _member['joined_at']
        self.is_pending = _member['is_pending']
        self.deaf = _member['deaf']
        self.avatar = _member["avatar"]
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
            "deaf": self.deaf,
            "avatar": self.avatar
        }

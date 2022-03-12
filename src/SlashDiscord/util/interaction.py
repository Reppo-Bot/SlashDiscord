"""Interaction class for responses to commands"""

from enum import IntEnum
from .user import Member

# Enums
class INTERACTION_CALLBACK_TYPES(IntEnum):
    PONG = 1 # ACK a ping
    CHANNEL_MESSAGE_WITH_SOURCE = 4 # response to an interaction with a message
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5 # ACK an interaction and edit a response later; does not see loading state
    DEFERRED_UPDATE_MESSAGE = 6 # for components, ACK an interaction and edit the original message later; does not see loading state; only available for component based interactions
    UPDATE_MESSAGE = 7 # for components, edit the message the component was originally attached to; does not see loading state; only available for component based interactions
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8 # respond to an autocomplete interaction with suggestions
    MODAL = 9 # respond to an interaction with a popup modal; not available for MODAL_SUBMIT and PING interactions

class CHANNEL_TYPES(IntEnum):
    GUILD_TEXT = 0
    DM = 1
    GUILD_VOICE = 2
    GROUP_DM = 3
    GUILD_CATEGORY = 4
    GUILD_NEWS = 5
    GUILD_STORE = 6
    GUILD_NEWS_THREAD = 10
    GUILD_PUBLIC_THREAD = 11
    GUILD_PRIVATE_THREAD = 12
    GUILD_STAGE_VOICE = 13

class MESSAGE_COMPONENT_TYPES(IntEnum):
    ACTION_ROW = 1
    BUTTON = 2
    SELECT_MENU = 3
    TEXT_INPUT = 4

class BUTTON_STYLES(IntEnum):
    PRIMARY = 1
    SECONDARY = 2
    SUCCESS = 3
    DANGER = 4
    LINK = 5

class TEX_INPUT_STYLES(IntEnum):
    SHORT = 1
    PARAGRAPH = 2

# classes

class InteractionData:
    ...

class InteractionResponse:
    ...

class InteractionCallbackData:
    type: int
    data: dict

class MessageComponent:
    type: int
    def __init__(self, type: int) -> None: ...
    def __iter__(self) -> dict: ...

class AllowedMentions:
    def __init__(self, parse: list() = None, roles: list() = None, users: list() = None, replied_user: bool = None):
        self.parse = parse
        self.roles = roles
        self.users = users
        self.replied_user = replied_user
    def __iter__(self) -> dict:
        return {
            "parse": self.parse,
            "roles": self.roles,
            "users": self.users,
            "replied_user": self.replied_user
        }

class Attachment:
    def __init__(self, id, filename, description, content_type = None, size = None, url = None, proxy_url = None, height = None, width = None, ephemeral = None):
        self.id = id
        self.filename = filename
        self.description = description
        self.content_type = content_type
        self.size = size
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width
        self.ephemeral = ephemeral
    def __iter__(self) -> dict:
        return {
            "id": self.id,
            "filename": self.filename,
            "description": self.description,
            "content_type": self.content_type,
            "size": self.size,
            "url": self.url,
            "proxy_url": self.proxy_url,
            "height": self.height,
            "width": self.width,
            "ephemeral": self.ephemeral
        }

class Message(InteractionCallbackData):
    def __init__(self, content = None, tts = None, embeds = None, allows_mentions = None, message_flags = None, components = None, attachments = None):
        self.content = content
        self.tts = tts
        self.embeds = embeds
        self.allows_mentions = allows_mentions
        self.message_flags = message_flags
        self.components = components
        self.attachments = attachments
    def __iter__(self) -> dict:
        return {
            "content": self.content,
            "tts": self.tts,
            "embeds": self.embeds,
            "allows_mentions": self.allows_mentions,
            "message_flags": self.message_flags,
            "components": self.components,
            "attachments": self.attachments
        }

class Modal(InteractionCallbackData):
    def __init__(self, custom_id, title, components):
        self.custom_id = custom_id
        self.title = title
        self.components = components
    def __iter__(self) -> dict:
        return {
            "custom_id": self.custom_id,
            "title": self.title,
            "components": self.components
        }

class Interaction:
    def __init__(self, payload):
        _payload = json.loads(payload) if type(payload) is str else payload
        self.version = _payload['version']
        self._type = _payload['type']
        self.member = Member(_payload['member'])
        self.id = _payload['id']
        self.token = _payload['token']
        self.guild_id = _payload['guild_id']
        self.channel_id = _payload['channel_id']
        self.data = _payload['data']


class ChannelMention:
    def __init__(self, id, guild_id, type, name):
        self.id = id
        self.guild_id = guild_id
        self.type = type
        self.name = name
    def __iter__(self):
        return {
            "id": self.id,
            "guild_id": self.guild_id,
            "type": self.type,
            "name": self.name
        }

class ActionRow(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.ACTION_ROW
    components: list()

class PartialEmoji:
    def __init__(self, name, id, animated):
        self.name = name
        self.id = id
        self.animated = animated
    def __iter__(self):
        return {
            "name": self.name,
            "id": self.id,
            "animated": self.animated
        }

class Button(MessageComponent):
    def __init__(self, style, label, emoji, custom_id, url, disabled = False):
        self.style = style
        self.label = label
        self.emoji = emoji
        self.custom_id = custom_id
        self.url = url
        self.disabled = disabled

    def __iter__(self):
        return {
            "style": self.style,
            "label": self.label,
            "emoji": self.emoji,
            "custom_id": self.custom_id,
            "url": self.url,
            "disabled": self.disabled
        }

class SelectOption:
    def __init__(self, label, value, description, emoji, default):
        self.label = label
        self.value = value
        self.description = description
        self.emoji = emoji
        self.default = default
    def __iter__(self) -> dict:
        return {
            "label": self.label,
            "value": self.value,
            "description": self.description,
            "emoji": self.emoji,
            "default": self.default
        }

class SelectMenu(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.SELECT_MENU
    custom_id: str
    options: list()
    placeholder: str
    min_values: int
    max_values: int
    disabled: bool = False
    def __init__(self, custom_id, options, placeholder, min_values, max_values, disabled = False):
        self.custom_id = custom_id
        self.options = options
        self.placeholder = placeholder
        self.min_values = min_values
        self.max_values = max_values
        self.disabled = disabled
    def __iter__(self):
        return {
            "custom_id": self.custom_id,
            "options": self.options,
            "placeholder": self.placeholder,
            "min_values": self.min_values,
            "max_values": self.max_values,
            "disabled": self.disabled
        }

class TextInput(MessageComponent):
    def __init__(self, custom_id, style, label, min_length, max_length, required, value, placeholder):
        self.custom_id = custom_id
        self.style = style
        self.label = label
        self.min_length = min_length
        self.max_length = max_length
        self.required = required
        self.value = value
        self.placeholder = placeholder
    def __iter__(self):
        return {
            "custom_id": self.custom_id,
            "style": self.style,
            "label": self.label,
            "min_length": self.min_length,
            "max_length": self.max_length,
            "required": self.required,
            "value": self.value,
            "placeholder": self.placeholder
        }

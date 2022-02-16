"""Interaction class for responses to commands"""

from slashReppo.util.bitfield import Bitfield
from slashReppo.util.embed import Embed
from slashReppo.util.user import Member
from enum import IntEnum

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
    parse: list(str)
    roles: list(str)
    users: list(str)
    replied_user: bool
    def __init__(self, parse: list(str) = None, roles: list(str) = None, users: list(str) = None, replied_user: bool = None) -> None: ...
    def __iter__(self) -> dict: ...

class Attachment:
    id: str
    filename: str
    description: str
    content_type: str = None
    size: int = None
    url: str = None
    proxy_url: str = None
    height: int = None
    width: int = None
    ephemeral: bool = None
    def __init__(self, id: str, filename: str, description: str, content_type: str = None, size: int = None, url: str = None, proxy_url: str = None, height: int = None, width: int = None, ephemeral: bool = None) -> None: ...
    def __iter__(self) -> dict: ...

class Message(InteractionCallbackData):
    type: int = INTERACTION_CALLBACK_TYPES.MESSAGE
    tts: bool = None
    content: str = None
    embeds: list(Embed) = None
    allows_mentions: list(AllowedMentions) = None
    message_flags: Bitfield
    components: list(MessageComponent) = None
    attachments: list(Attachment) = None
    def __init__(self, content: str = None, tts: bool = None, embeds: list(Embed) = None, allows_mentions: list = None, message_flags: Bitfield = None, components: list = None, attachments: list = None) -> None: ...
    def __iter__(self) -> dict: ...

class Autocomplete(InteractionCallbackData):
    type: int = INTERACTION_CALLBACK_TYPES.AUTOCOMPLETE
    def __iter__(self) -> dict: ...

class Modal(InteractionCallbackData):
    type: int = INTERACTION_CALLBACK_TYPES.MODAL
    custom_id: str
    title: str
    components: list(MessageComponent)
    def __init__(self, custom_id: str, title: str, components: list(MessageComponent)) -> None: ...
    def __iter__(self) -> dict: ...

class Interaction:
    _type: int = None
    member: Member = None
    id: str = None
    guild_id: str = None
    channel_id: str = None
    data: dict = None
    def __init__(self, type: int, member: Member, id: str, guild_id: str = None, channel_id: str = None, data: dict = None) -> None: ...
    def send(messsage: Message = None, autocomplete: Autocomplete = None, modal: Modal = None) -> None: ...

class ChannelMention:
    id: str = None
    guild_id: str
    type: int
    name: str # name of channel
    def __init__(self, id: str, guild_id: str, type: int, name: str) -> None: ...
    def __iter__(self) -> dict: ...

class ActionRow(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.ACTION_ROW
    components: list(MessageComponent)

class PartialEmoji:
    name: str
    id: str
    animated: bool
    def __init__(self, name: str, id: str, animated: bool) -> None: ...
    def __iter__(self) -> dict: ...

class Button(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.BUTTON
    style: int
    label: str
    emoji: PartialEmoji
    custom_id: str
    url: str
    disabled: bool = False
    def __init__(self, style: int, label: str, emoji: PartialEmoji, custom_id: str, url: str, disabled: bool = False) -> None: ...
    def __iter__(self) -> dict: ...

class SelectOption:
    label: str
    value: str
    description: str
    emoji: PartialEmoji
    default: bool
    def __init__(self, label: str, value: str, description: str, emoji: PartialEmoji, default: bool) -> None: ...
    def __iter__(self) -> dict: ...

class SelectMenu(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.SELECT_MENU
    custom_id: str
    options: list(SelectOption)
    placeholder: str
    min_values: int
    max_values: int
    disabled: bool = False
    def __init__(self, custom_id: str, options: list, placeholder: str, min_values: int, max_values: int, disabled: bool = False) -> None: ...
    def __iter__(self) -> dict: ...

class TextInput(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.TEXT_INPUT
    custom_id: str
    style: int
    label: str
    min_length: int
    max_length: int
    required: bool
    value: str
    placeholder: str
    def __init__(self, custom_id: str, style: int, label: str, min_length: int, max_length: int, required: bool, value: str, placeholder: str) -> None: ...
    def __iter__(self) -> dict: ...

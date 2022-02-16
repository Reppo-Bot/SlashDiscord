"""Interaction class for responses to commands"""

from pydoc import describe
from typing import Any, OrderedDict
from slashReppo.util.bitfield import Bitfield
from slashReppo.util.user import Member
from enum import Enum

class Interaction:
    _type: int = None
    member: Member = None
    id: str = None
    guild_id: str = None
    channel_id: str = None
    data: dict = None
    def __init__(self, type: int, member: Member, id: str, guild_id: str = None, channel_id: str = None, data: dict = None) -> None: ...
    def send(socket, data: dict) -> None: ...

class InteractionData(OrderedDict):
    ...

class InteractionResponse(OrderedDict):
    ...

class InteractionCallbackData(OrderedDict):
    type: int
    data: dict

class Message(InteractionCallbackData):
    type: int = INTERACTION_CALLBACK_TYPES.MESSAGE
    tts: bool = None
    content: str = None
    embeds: list(Embed) = None
    allows_mentions: list(AllowedMentions) = None
    message_flags: Bitfield
    components: list(MessageComponent) = None
    attachments: list(Attachment) = None

class Autocomplete(InteractionCallbackData):
    type: int = INTERACTION_CALLBACK_TYPES.AUTOCOMPLETE

class Modal(InteractionCallbackData):
    type: int = INTERACTION_CALLBACK_TYPES.MODAL
    custom_id: str
    title: str
    components: list(MessageComponent)


class INTERACTION_CALLBACK_TYPES(Enum):
    PONG = 1 # ACK a ping
    CHANNEL_MESSAGE_WITH_SOURCE = 4 # response to an interaction with a message
    DEFERRED_CHANNEL_MESSAGE_WITH_SOURCE = 5 # ACK an interaction and edit a response later; does not see loading state
    DEFERRED_UPDATE_MESSAGE = 6 # for components, ACK an interaction and edit the original message later; does not see loading state; only available for component based interactions
    UPDATE_MESSAGE = 7 # for components, edit the message the component was originally attached to; does not see loading state; only available for component based interactions
    APPLICATION_COMMAND_AUTOCOMPLETE_RESULT = 8 # respond to an autocomplete interaction with suggestions
    MODAL = 9 # respond to an interaction with a popup modal; not available for MODAL_SUBMIT and PING interactions

class EmbedFooter(OrderedDict):
    text: str = None
    icon_url: str = None
    proxy_icon_url: str = None

class EmbedImage(OrderedDict):
    url: str = None
    proxy_url: str = None
    height: int = None
    width: int = None

class EmbedProvider(OrderedDict):
    name: str = None
    url: str = None

class EmbedAuthor(OrderedDict):
    name: str = None
    url: str = None
    icon_url: str = None
    proxy_icon_url: str = None

class EmbedField:
    name: str = None
    value: str = None
    inline: bool = None

class Embed(OrderedDict):
    title: str
    type: str
    description: str
    url: str
    timestamp: Any
    color: int = None
    footer: EmbedFooter
    image: EmbedImage
    thumbnail: EmbedImage
    video: EmbedImage
    provider: EmbedProvider
    author: EmbedAuthor
    fields: list(EmbedField)

class ChannelMention(OrderedDict):
    id: str = None
    guild_id: str
    type: int
    name: str # name of channel

class AllowedMentions(OrderedDict):
    parse: list(str)
    roles: list(str)
    users: list(str)
    replied_user: bool

class CHANNEL_TYPES(Enum):
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

class Attachment(OrderedDict):
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

class MessageComponent(OrderedDict):
    type: int

class MESSAGE_COMPONENT_TYPES(Enum):
    ACTION_ROW = 1
    BUTTON = 2
    SELECT_MENU = 3
    TEXT_INPUT = 4

class ActionRow(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.ACTION_ROW
    components: list(MessageComponent)

class Button(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.BUTTON
    style: int
    label: str
    emoji: PartialEmoji
    custom_id: str
    url: str
    disabled: bool = False

class PartialEmoji(OrderedDict):
    name: str
    id: str
    animated: bool

class BUTTON_STYLES(Enum):
    PRIMARY = 1
    SECONDARY = 2
    SUCCESS = 3
    DANGER = 4
    LINK = 5

class SelectMenu(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.SELECT_MENU
    custom_id: str
    options: list(SelectOption)
    placeholder: str
    min_values: int
    max_values: int
    disabled: bool = False

class SelectOption(OrderedDict):
    label: str
    value: str
    description: str
    emoji: PartialEmoji
    default: bool

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

class TEX_INPUT_STYLES(Enum):
    SHORT = 1
    PARAGRAPH = 2

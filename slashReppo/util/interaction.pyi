"""Interaction class for responses to commands"""

from typing import Any, OrderedDict
from slashReppo.util.bitfield import Bitfield
from slashReppo.util.user import Member
from enum import IntEnum

class INTERACTION_CALLBACK_TYPES(IntEnum): ...

class CHANNEL_TYPES(IntEnum): ...

class MESSAGE_COMPONENT_TYPES(IntEnum): ...

class BUTTON_STYLES(IntEnum): ...

class TEX_INPUT_STYLES(IntEnum): ...

class Interaction:
    _type: int = None
    member: Member = None
    id: str = None
    guild_id: str = None
    channel_id: str = None
    data: dict = None
    def __init__(self, type: int, member: Member, id: str, guild_id: str = None, channel_id: str = None, data: dict = None) -> None: ...
    def send(messsage: Message) -> None: ...
    def send(autocomplete: Autocomplete) -> None: ...
    def send(modal: Modal) -> None: ...

class InteractionData:
    ...

class InteractionResponse:
    ...

class InteractionCallbackData:
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

class EmbedFooter:
    text: str = None
    icon_url: str = None
    proxy_icon_url: str = None
    def __init__(self, text: str = None, icon_url: str = None, proxy_icon_url: str = None) -> None: ...
    def __iter__(self) -> dict: ...

class EmbedImage:
    url: str = None
    proxy_url: str = None
    height: int = None
    width: int = None
    def __init__(self, url: str = None, proxy_url: str = None, height: int = None, width: int = None) -> None: ...
    def __iter__(self) -> dict: ...

class EmbedProvider:
    name: str = None
    url: str = None
    def __init__(self, name: str = None, url: str = None) -> None: ...
    def __iter__(self) -> dict: ...

class EmbedAuthor(OrderedDict):
    name: str = None
    url: str = None
    icon_url: str = None
    proxy_icon_url: str = None
    def __init__(self, name: str = None, url: str = None, icon_url: str = None, proxy_icon_url: str = None) -> None: ...
    def __iter__(self) -> dict: ...

class EmbedField:
    name: str = None
    value: str = None
    inline: bool = None
    def __init__(self, name: str = None, value: str = None, inline: bool = None) -> None: ...
    def __iter__(self) -> dict: ...

class Embed:
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
    def __init__(self, title: str, type: str, description: str, url: str, timestamp: Any, color: int = None, footer: EmbedFooter = None, image: EmbedImage = None, thumbnail: EmbedImage = None, video: EmbedImage = None, provider: EmbedProvider = None, author: EmbedAuthor = None, fields: list(EmbedField) = None) -> None: ...
    def __iter__(self) -> dict: ...

class ChannelMention:
    id: str = None
    guild_id: str
    type: int
    name: str # name of channel
    def __init__(self, id: str, guild_id: str, type: int, name: str) -> None: ...
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

class MessageComponent:
    type: int
    def __init__(self, type: int) -> None: ...
    def __iter__(self) -> dict: ...

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
    def __init__(self, style: int, label: str, emoji: PartialEmoji, custom_id: str, url: str, disabled: bool = False) -> None: ...
    def __iter__(self) -> dict: ...

class PartialEmoji:
    name: str
    id: str
    animated: bool
    def __init__(self, name: str, id: str, animated: bool) -> None: ...
    def __iter__(self) -> dict: ...

class SelectMenu(MessageComponent):
    type: int = MESSAGE_COMPONENT_TYPES.SELECT_MENU
    custom_id: str
    options: list(SelectOption)
    placeholder: str
    min_values: int
    max_values: int
    disabled: bool = False
    def __init__(self, custom_id: str, options: list(SelectOption), placeholder: str, min_values: int, max_values: int, disabled: bool = False) -> None: ...
    def __iter__(self) -> dict: ...

class SelectOption:
    label: str
    value: str
    description: str
    emoji: PartialEmoji
    default: bool
    def __init__(self, label: str, value: str, description: str, emoji: PartialEmoji, default: bool) -> None: ...
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
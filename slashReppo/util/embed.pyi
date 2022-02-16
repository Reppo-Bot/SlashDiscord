"""Embed Classes"""
from typing import Any, OrderedDict
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
class EmbedFooter:
    def __init__(self, text=None, icon_url=None, proxy_icon_url=None):
        self.text = text
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

    def __iter__(self):
        return {
            "text": self.text,
            "icon_url": self.icon_url,
            "proxy_icon_url": self.proxy_icon_url
        }

class EmbedImage:
    def __init__(self, url=None, proxy_url=None, height=None, width=None):
        self.url = url
        self.proxy_url = proxy_url
        self.height = height
        self.width = width

    def __iter__(self):
        return {
            "url": self.url,
            "proxy_url": self.proxy_url,
            "height": self.height,
            "width": self.width
        }

class EmbedProvider:
    def __init__(self, name=None, url=None):
        self.name = name
        self.url = url

    def __iter__(self):
        return {
            "name": self.name,
            "url": self.url
        }

class EmbedAuthor:
    def __init__(self, name=None, url=None, icon_url=None, proxy_icon_url=None):
        self.name = name
        self.url = url
        self.icon_url = icon_url
        self.proxy_icon_url = proxy_icon_url

    def __iter__(self):
        return {
            "name": self.name,
            "url": self.url,
            "icon_url": self.icon_url,
            "proxy_icon_url": self.proxy_icon_url
        }

class EmbedField:
    def __init__(self, name=None, value=None, inline=None):
        self.name = name
        self.value = value
        self.inline = inline

    def __iter__(self):
        return {
            "name": self.name,
            "value": self.value,
            "inline": self.inline
        }

class Embed:
    def __init__(self, title, type, description, url, timestamp, color=None, footer=None, image=None, thumbnail=None, video=None, provider=None, author=None, fields=None):
        self.title = title
        self.type = type
        self.description = description
        self.url = url
        self.timestamp = timestamp
        self.color = color
        self.footer = footer
        self.image = image
        self.thumbnail = thumbnail
        self.video = video
        self.provider = provider
        self.author = author
        self.fields = fields

    def __iter__(self) -> dict:
        return {
            "title": self.title,
            "type": self.type,
            "description": self.description,
            "url": self.url,
            "timestamp": self.timestamp,
            "color": self.color,
            "footer": self.footer,
            "image": self.image,
            "thumbnail": self.thumbnail,
            "video": self.video,
            "provider": self.provider,
            "author": self.author,
            "fields": self.fields
        }
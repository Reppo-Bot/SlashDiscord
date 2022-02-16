
"""For managing the gateway"""

from enum import IntEnum, Flag
from typing import OrderedDict

GATEWAY_VERSION = 9

class GATEWAY_OPCODES(IntEnum): ...

class GATEWAY_CLOSE_CODES(IntEnum): ...

class VOICE_OPCODES(IntEnum): ...

class VOICE_CLOSE_EVENT_CODES(IntEnum): ...

class JSON_CODES(IntEnum): ...

class RPC_ERROR_CODES(IntEnum): ...

class RPC_CLOSE_EVENT_CODES(IntEnum): ...

class GATEWAY_INTENTS(Flag): ...

class Payload(OrderedDict):
    op: int = None # opcode
    d: dict = None # data
    s: int = None # seq num
    t: str = None # event name

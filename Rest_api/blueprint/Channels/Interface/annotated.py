from typing import TypedDict, Required, NotRequired

class Data(TypedDict):
    channel_name: Required[str]
    message: NotRequired[str]
    success: Required[bool]
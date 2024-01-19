from typing import TypedDict, Required, NotRequired

class Data(TypedDict):
    video_name: Required[str]
    message: NotRequired[str]
    success: Required[bool]
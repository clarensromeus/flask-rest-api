from typing import TypedDict, Required, NotRequired

class Data(TypedDict):
    Firstname: Required[str]
    Lastname: Required[str]
    Message: NotRequired[str]
    success: NotRequired[bool]
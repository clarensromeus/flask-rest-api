from __future__ import annotations

from  pydantic import BaseModel, Field, ConfigDict, EmailStr, StrictStr, StrictInt
from typing import Annotated, List, TYPE_CHECKING
import random

if TYPE_CHECKING:
    from Rest_api.blueprint.Videos.video_validation.validation import VideoResponse
    from Rest_api.blueprint.Channels.channel_validation.validation import ChannelResponse
    
    
class UserCreation(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validation_error_cause=True)
    
    Firstname: Annotated[str, Field("Larry", max_length=40, min_length=5, title="USER_FIRSTNAME", description="USER FIRSNAME",
                                    examples=["MARK", "ANTHONY"], validate_default=True)]
    Lastname: Annotated[str, Field("Ellison", max_length=40, min_length=5, title="USER_LASTNAME", description="USER LASTNAME",
                                   examples=["ZUCKERBERG"], validate_default=True)]
    Password: Annotated[str, Field("Thomas(+-1844)", max_length=50, min_length=8, title="USER_PASSWORD",
                                   description="USER PASSWORD")]
    Email: EmailStr = Field("romeusclarens@gmail.com", validate_default=True, title="USER_EMAIL",
                            description="USER DESCRIPTION", examples=["username33@gmail.com"])
    Proffession: StrictStr = Field("Software engineer", frozen=True, title="USER_PROFFESSION", description="USER PROFFESSION",
                                          validate_default=True, )
    NetWorth: StrictInt = Field(5000, gt=100, le=50, title="NET_WORTH",description="user net worth")
    
    
class UserResponse(UserCreation):
    model_config = ConfigDict(strict=True)
    
    id: Annotated[int, Field(random.randint(1, 100), le=100, gt=0, title="USER_ID",description="UNIQUE AND ORDERED USER ID", 
                             examples=1, validate_default=True)]
    Videos: VideoResponse = Field(default_factory=list, title="USER_VIDEOS", serialization_alias="user_videos",
                           description="ALL USER VIDEOS")
    Channels: List[ChannelResponse] = Field(default_factory=list, title="USER_CHANNELS", serialization_alias='user_channels', 
                           description="ALL USER CHANNELS")
    
class UserUpdate(BaseModel):
    model_config = ConfigDict(validation_error_cause=True, extra="forbid")
    
    Firstname: StrictStr = Field("romeus", max_length=40, min_length=6, validate_default=True)
    Lastname: StrictStr =  Field("clarens", max_length=40, min_length=6, validate_default=True)
    Password: str = Field("Clarens(+-1998)", max_length=70, min_length=6, validate_default=True)
    
    
class UserList(BaseModel):
    Users: List[UserResponse] = Field(default_factory=list, max_length=1000, min_length=1, title="ALL_PLATFORM_USERS",
                                      description="all users of the in-place platform")

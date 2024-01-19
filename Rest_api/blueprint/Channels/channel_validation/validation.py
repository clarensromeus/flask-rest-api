from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, StrictInt
from typing import Annotated, List, TYPE_CHECKING
import random
from datetime import datetime


if TYPE_CHECKING:
    from Rest_api.blueprint.Users.user_validation.validation import UserResponse


class Query_model(BaseModel):
    user_id: StrictInt = 2

class ChannelCreation(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid", validation_error_cause=True)
    
    Channel_name: Annotated[str, Field("Winner mindset", max_length=50, min_length=5, title="CHANNEL_NAME", description="the channel's name",
                                       validate_default=True, examples=["Five laws of power", "Life principles"])]
    Channel_description: Annotated[str, Field("never wasting time", max_length=200, min_length=10, title="CHANNEL_DESCRIPTION",
                                              description="brief channel description", validate_default=True)]
    

class ChannelResponse(ChannelCreation):

    id: Annotated[int, Field(random.randint(1, 100), le=100, gt=0, title="USER_ID",description="UNIQUE AND ORDERED USER ID", 
                             examples=[1, 30, 4, 49], validate_default=True)]
    created_at: datetime = Field(default=datetime.utcnow, title="CHANNEL_CREATION_TIME", 
                                 description="the date creation of the channel", validate_default=True,)
    updated_at: datetime = Field(default=datetime.utcnow, title="CHANNEL_CREATION_UPDATE_TIME",
                                 description="the modification time of the channel", validate_default=True)
    followers: List[UserResponse] = Field(default_factory=list, title="CHANNEL_FOLLOWERS", description="all the channel followers",
                            validate_default=True)
    
    
class ChannelUpdate(BaseModel):
    model_config = ConfigDict(validation_error_cause=True, extra="forbid")
    
    Channel_name: StrictStr =  Field(default="Winner mindset", max_length=50, min_length=5, title="CHANNEL_NAME")
    Channel_description: StrictStr = Field(default="get it going right now ", max_length=50, min_length=10, title="DESCRIPTION")


class ChannelList(BaseModel):
    Channels: List[ChannelResponse]
from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field, StrictStr, StrictInt
from typing import Annotated, TYPE_CHECKING, Any
import random
from datetime import datetime



if TYPE_CHECKING:
    from Rest_api.blueprint.Users.user_validation.validation import UserResponse
    

class Query_model(BaseModel):
    user_id: StrictInt = 2

class VideoCreation(BaseModel):
    # global model config
    model_config = ConfigDict(strict=True, revalidate_instances="always", validation_error_cause=True)
    
    Video_name: Annotated[str, Field("Amaguedon", max_length=200, min_length=5, title="VIDEO_NAME", 
                                     description="VIDEO_DESCRIPTION", validate_default=True, examples=["Soccer", "Basketball", "Tennis"])]
    Video_title: Annotated[str, Field("the last world war", max_length=200, min_length=10, title="VIDEO_TITLE",
                                      description="VIDEO TITLE", validate_default=True)]
    
       
class VideoResponse(VideoCreation):
    
    id: Annotated[int, Field(random.randint(1, 100),strict=True, title="VIDEO_ID", description="VIDEO ID",
                             validate_default=True)]
    user: UserResponse = Field(default_factory=lambda: dict, title="VIDEO_USERS", description="all video users", validate_default=True)
    created_at: datetime = Field(default=datetime.utcnow, title="VIDEO_CREATION_TIME", 
                                 description="the date creation of the channel", validate_default=True,)
    updated_at: datetime = Field(default=datetime.utcnow, title="VIDEO_CREATION_UPDATE_TIME",
                                 description="the modification time of the video", validate_default=True)
    
     
class VideoUpdate(BaseModel):
    model_config = ConfigDict(validation_error_cause=True, extra="forbid")
    
    Video_name: StrictStr = Field("Postponer", max_length=50, min_length=5, validate_default=True, strict=True)
    Video_title: StrictStr = Field("don't see only the shiny side of the sun", max_length=200, min_length=10,
                                   validate_default=True, strict=True)

class VideoList(BaseModel):
    videos: list[VideoResponse]

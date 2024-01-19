from flask import abort
from flask_pydantic import validate 
from flask_restful import Resource
from Rest_api.blueprint.Videos.video_model.model import VideoTable
from Rest_api.blueprint.Users.user_model.model import UserTable
from Rest_api.blueprint.Videos.video_validation.validation import VideoCreation, VideoResponse,VideoList,Query_model
from typing import List
from Rest_api import db

class Videos(Resource):
    @validate(on_success_status=True, response_many=True)
    def get(self):
        data: List[VideoResponse] =  VideoTable.query.all()
        if len(data) < 1:
            abort(404, "no video registered in yet")
        validate_video_data = VideoList(Users=data).model_dump_json(exclude_unset=True)
        return validate_video_data
    
    @validate(on_success_status=True, request_body_many=True)
    def Post(self, body: VideoCreation, video_name: str, query: Query_model):
        video = VideoTable.query.filter_by(Video_name=video_name).first()
        user: UserTable = UserTable.query.filter_by(id=query.user_id).first()
        if video is not None:
            abort(404, "sorry, video already exists")
        new_video = VideoTable(Video_name=body.Video_name, Video_title=body.Video_title, user=user)
        db.session.add(new_video)
        db.session.commit()
        data_serialization = VideoResponse(
            id=new_video.id,
            Video_name=new_video.Video_name,
            Video_title=new_video.Video_title,
            created_at=new_video.created_at,
            updated_at=new_video.updated_at,
            user=new_video.user
            ).model_dump(by_alias=True, mode="json",exclude_unset=True)
        return data_serialization
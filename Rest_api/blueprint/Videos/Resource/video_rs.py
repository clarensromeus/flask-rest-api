from __future__ import annotations

from flask import abort, jsonify
from flask_restful import Resource
from flask_pydantic import validate
from Rest_api.blueprint.Videos.video_model.model import VideoTable
from Rest_api.blueprint.Videos.video_validation.validation import VideoResponse, VideoUpdate
from Rest_api import db
from Rest_api.blueprint.Videos.Interface.annotated import Data

class Video(Resource):    
    @validate(on_success_status=201,response_many=False)
    def get(self, video_id: int):
        video: VideoTable = VideoTable.query.filter_by(id=video_id).first()
        if not video_id and video is None:
            abort(404, "sorry either no video specified or the video not exists")  
        data_serialization = VideoResponse(
            id=video.id,
            user=video.user,
            Video_name=video.Video_name,
            Video_title=video.Video_title,
            created_at=video.created_at,
            updated_at=video.updated_at,
            ).model_dump(mode="json", exclude_none=True)
        return data_serialization, 201
    
    @validate(on_success_status=201, response_many=False)
    def put(self, video_id: int, body: VideoUpdate):
        video: VideoTable = VideoTable.query.filter_by(id=video_id).first()
        if not video_id and video is None:
            abort(404, "sorry either no video specified or the video not exists")
        video.Video_name = body.Video_name
        video.Video_title = body.Video_title
        db.session.commit()
        video_serialization = VideoResponse(
            id=video.id,
            Video_name=video.Video_name,
            Video_title=video.Video_title,
            created_at=video.created_at,
            updated_at=video.updated_at,
            ).model_dump(mode="json", exclude_unset=True)
        return video_serialization, 201

    @validate(on_success_status=201, response_many=False)
    def delete(self, video_id: int):
        video: VideoTable = VideoTable.query.filter_by(id=video_id).first()
        data: Data = {"video_name": '', "success": False}
        if not video_id and video is None:
            abort(404, "sorry, either no video specified or the video not exists")
        data["video_name"] = video.Video_name
        data["success"] = True
        db.session.delete(video)
        db.session.commit()
        return jsonify({"message": "video %s deleted with success" % data["video_name"]}), 201

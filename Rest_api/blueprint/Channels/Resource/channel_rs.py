from flask_restful import Resource
from flask import abort, jsonify
from flask_pydantic import validate
from Rest_api.blueprint.Channels.channel_model.model import ChannelTable
from Rest_api.blueprint.Channels.channel_validation.validation import  ChannelResponse, ChannelUpdate
from Rest_api.blueprint.Channels.Interface.annotated import Data
from Rest_api import db

class Channel(Resource):
    @validate(on_success_status=201, response_many=False)
    def get(self, channel_id: int):
        channel: ChannelTable = ChannelTable.query.filter_by(id=channel_id).first()
        if not channel_id and channel is None:
            abort(404, "sorry, either no channel specified or channel not exists")  
        data_serialization = ChannelResponse(
            id=channel.id,
            Channel_name=channel.Channel_name,
            Channel_description=channel.Channel_description,
            created_at=channel.created_at,
            updated_at=channel.updated_at,
            followers=channel.followers
            ).model_dump(mode="json", exclude_none=True)
        return data_serialization, 201
    
    @validate(on_success_status=201)
    def put(self, channel_id: int, body: ChannelUpdate):
        channel: ChannelTable = ChannelTable.query.filter_by(id=channel_id).first()
        if not channel_id and channel is None:
            abort(404, "sorry, either no channel specified or channel not exists")
        channel.Video_name = body.Channel_name
        channel.Channel_description = body.Channel_description
        db.session.commit()
        channel_serialization = ChannelResponse(
            id=channel.id,
            Channel_name=channel.Channel_name,
            Channel_description=channel.Channel_description,
            created_at=channel.created_at,
            updated_at=channel.updated_at,
            followers=channel.followers
            ).model_dump(mode="json", exclude_unset=True)
        return channel_serialization, 201
    
    @validate(on_success_status=201)
    def delete(self, channel_id: int):
        channel: ChannelTable = ChannelTable.query.filter_by(id=channel_id).first()
        data: Data = {"channel_name": '', "success": False}
        if not channel_id and channel is None:
            abort(404, "sorry, either no channel specified or channel not exists")
        data["channel_name"] = channel.Channel_name
        data["success"] = True
        db.session.delete(channel)
        db.session.commit()
        return jsonify({"message": "video %s deleted with success" % data["channel_name"]}), 201
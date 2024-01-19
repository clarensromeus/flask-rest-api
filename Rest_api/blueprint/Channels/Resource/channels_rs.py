from flask import abort
from flask_pydantic import validate
from flask_restful import Resource
from Rest_api.blueprint.Channels.channel_model.model import ChannelTable
from Rest_api.blueprint.Channels.channel_validation.validation import ChannelResponse, \
ChannelCreation, ChannelList, Query_model
from Rest_api.blueprint.Users.user_model.model import UserTable
from typing import List
from Rest_api import db

class Channels(Resource):
    @validate(on_success_status=201, response_many=True)
    def get(self):
        channels: List[ChannelResponse] = ChannelTable.query.all()
        if len(channels) < 1:
            abort(404, "no channel registered in yet")
        validate_channels_data = ChannelList(Channels=Channels).model_dump_json(exclude_none=True)
        return validate_channels_data, 201
        
    @validate(on_success_status=201, request_body_many=True)
    def post(self, body: ChannelCreation, channel_name: str, query: Query_model):
        channel: ChannelTable = ChannelTable.query.filter_by(Channel_name=channel_name).first()
        user: UserTable = UserTable.query.filter_by(id=query.user_id)
        if channel is not None:
            abort(404, "sorry, channel by that name alredy exists")
        new_channel = ChannelTable(Channel_name=body.Channel_name, Channel_description=body.Channel_description)
        new_channel.followers.append(user)
        db.session.add(new_channel)
        db.session.commit()
        data_serialization = ChannelResponse(
            id=new_channel.id,
            Channel_name=new_channel.Channel_name,
            Channel_description=new_channel.Channel_description,
            created_at=new_channel.created_at,
            updated_at=new_channel.updated_at,
            followers=new_channel.followers
            ).model_dump(by_alias=True, mode="json", exclude_unset=True)
        return data_serialization, 201
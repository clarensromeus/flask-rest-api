from Rest_api import app
from Rest_api.blueprint.Channels.Resource.channel_rs import Channel
from Rest_api.blueprint.Channels.Resource.channels_rs import Channels
from Rest_api.blueprint.Channels.channels_bp import channels_bp, channel_bp, channel_api, channels_api
from Rest_api.blueprint.Users.Resource.user_rs import User
from Rest_api.blueprint.Users.Resource.users_rs import Users
from Rest_api.blueprint.Users.users_bp import user_api, users_api, Users_bp, User_bp
from Rest_api.blueprint.Videos.Resource.video_rs import Video
from Rest_api.blueprint.Videos.Resource.videos_rs import Videos
from Rest_api.blueprint.Videos.videos_bp import video_api, videos_bp, video_bp, videos_api

# add users's Apis
users_api.add_resource(Users, '/')
user_api.add_resource(User, '/<int:user_id>')

# add channel's Apis
channels_api.add_resource(Channels, '/channels')
channel_api.add_resource(Channel, '/channels/<int:channel_id>')

# add videos's Apis
videos_api.add_resource(Videos, '/videos')
video_api.add_resource(Video, '/videos/<int:video_id>')

# register users' Blueprint
app.register_blueprint(Users_bp)
app.register_blueprint(User_bp)

# register channels' Blueprint
app.register_blueprint(channels_bp)
app.register_blueprint(channel_bp) 

# register videos' Blueprint
app.register_blueprint(videos_bp)
app.register_blueprint(video_bp)
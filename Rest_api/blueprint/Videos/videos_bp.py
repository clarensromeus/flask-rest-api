from flask import Blueprint
from flask_restful import Api

# videos Blueprints
video_bp: Blueprint = Blueprint("video_bp", __name__)
videos_bp: Blueprint = Blueprint("videos_bp", __name__)

# videos Apis
video_api: Api = Api(video_bp)
videos_api: Api = Api(videos_bp)
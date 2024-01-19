from flask_restful import Resource
from flask import jsonify, abort
from flask_pydantic import validate
from Rest_api.blueprint.Users.user_validation.validation import UserResponse, UserUpdate
from Rest_api.blueprint.Users.user_model.model import UserTable
#from annotated_types import Gt, Predicate, IsFinite
from Rest_api import db
from Rest_api.blueprint.Users.interface.annotated import Data

class User(Resource):
    @validate(on_success_status=201, response_many=False)
    def get(self, user_id: int):
        user = UserTable.query.filter_by(id=user_id).first()
        if not user_id and user is None:
            abort(404, "sorry, either no user specified or user not exists")  
        data_serialization = UserResponse(
            id=user.id,
            Firstname=user.Firstname,
            Lastname=user.Lastname,
            Password=user.Password,
            Email=user.Email,
            Proffession=user.Proffession,
            NetWorth=user.NetWorth,
            Videos=user.Videos,
            Channels=user.Channels
            ).model_dump(mode="json", exclude_none=True)
        return data_serialization
        
    @validate(on_success_status=201, response_many=False)
    def put(self, user_id, body: UserUpdate):
        user = UserTable.query.filter_by(id=user_id).first()
        if not user_id and user is None:
            abort(404, "sorry, either no user specified or user not exists ")
        user.Firstname = body.Firstname
        user.Lastname = body.Lastname
        user.Password = body.Password
        db.session.commit()
        data_serialization = UserResponse(
            id=user.id,
            Firstname=user.Firstname,
            Lastname=user.Lastname,
            Email=user.Email,
            Password=user.Password,
            Proffession=user.Proffession,
            NetWorth=user.NetWorth,
            Videos=user.Videos,
            Channels=user.Channels
        )
        return data_serialization, 201
        
    @validate(on_success_status=201, response_many=False)
    def delete(self, user_id: int):
        user: UserResponse = UserTable.query.filter_by(id=user_id).first()
        data: Data = {"Firstname": '', "Lastname": ''}
        if not user_id and user is None:
            abort(404, "sorry, either no user specified or user not ")
        data["Firstname"] = user.Firstname
        data["Lastname"] = user.Lastname
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "user %s %s deleted with success" % (data["Firstname"], data["Lastname"])}), 201
        
            
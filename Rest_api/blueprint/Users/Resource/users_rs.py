from flask import abort
from flask_restful import Resource
from flask_pydantic import validate
from sqlalchemy.orm import Query
# internally crafted import of resources
from typing import Self
from Rest_api.blueprint.Users.user_model.model import UserTable
from Rest_api.blueprint.Users.user_validation.validation import UserResponse, UserList, UserCreation
from typing import List
from Rest_api import db

class Users(Resource):
    @validate(on_success_status=201, response_many=False, response_by_alias=True)
    def get(self):
        data: List[UserResponse] =  UserTable.query.all()
        if len(data) < 1:
            abort(404, "no users in registered yet")
        validate_user_data = UserList(Users=data).model_dump_json(exclude_unset=True)
        return validate_user_data
          
    @validate(on_success_status=201, response_many=False, response_by_alias=True, request_body_many=True)
    def post(self, body: UserCreation):
        query: Query = UserTable.query
        if not body:
            abort(400, "sorry no data provided")
        if (user := query.filter_by(Firstname=body.Firstname, Email=body.Email).first()) is not None:
            abort(404, "sorry %s %s already taken" % (user.Firstname, user.Lastname))
        newuser = UserTable(Firstname=body.Firstname, Lastname=body.Lastname, Email=body.Lastname,
                               Password=body.Password, Proffession=body.Proffession, NetWorth=body.NetWorth)
        db.session.add(newuser)
        db.session.commit()
        data_serialization = UserResponse(
            id = newuser.id,
            Firstname=newuser.Firstname,
            Lastname=newuser.Lastname,
            Password=newuser.Password,
            Proffession=newuser.Proffession,
            NetWorth=newuser.NetWorth,
            Email=newuser.Email
            ).model_dump(by_alias=True, mode="json", exclude_unset=True)
        return data_serialization
        
        

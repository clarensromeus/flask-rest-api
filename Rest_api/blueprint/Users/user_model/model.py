from Rest_api import db
from datetime import datetime
from typing import Self
from Rest_api.Helper.DB.Table.relashionship import Social


# SQLALQUEMY user model creation
# mypy: ignore-errors
class UserTable(db.Model): 
    id = db.Column("id",db.Integer, primary_key=True)
    Firstname = db.Column(db.String(200), nullable=False)
    Lastname  = db.Column(db.String(200), nullable=False, )
    Password  = db.Column(db.String(200), nullable=False, unique=True)
    Email  = db.Column(db.String(200), unique=True, nullable=False)
    Proffession  = db.Column(db.String(200), nullable=True)
    NetWorth = db.Column(db.Float, nullable=True, unique=False)
    Date_joined = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    Videos = db.relationship("VideoTable", backref=db.backref("user", lazy="joined"), lazy=True)
    Channels = db.relationship("ChannelTable", secondary=Social, lazy="subquery", backref=db.backref("followers", lazy=True))
    
    def __repr__(self: Self) -> str:
        return "User : %s" % self.Firstname
      
       
    def password_check(self: Self, newpassword: str):
      return self.password == newpassword
    

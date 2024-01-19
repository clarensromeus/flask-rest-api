from Rest_api import db
from datetime import datetime
from typing import Self


# mypy: ignore-errors
class ChannelTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    Channel_name = db.Column(db.String(200), nullable=False, unique=True)
    Channel_description = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self: Self) -> str:
        return "Channel : %s" % self.Channel_name
    
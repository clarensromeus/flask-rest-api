from Rest_api import db
from datetime import datetime

# mypy: ignore-errors
class VideoTable(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    Video_name = db.Column(db.String(200), nullable=False, unique=True)
    Video_title = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_table.id'), nullable=False)
    
    
    def __repr__(self) -> str:
        return "Video : %s" % self.Video_name
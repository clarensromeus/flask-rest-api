from Rest_api import db

Social = db.Table(
    "Social",
    db.Column('user_id', db.Integer, db.ForeignKey('user_table.id'), primary_key=True),
    db.Column('channel_id', db.Integer, db.ForeignKey('channel_table.id'), primary_key=True)
)
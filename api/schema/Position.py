from db import db
from datetime import datetime


class Position(db.Model):
    __tablename__ = "houmer_position"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    time_registry = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "<Position {}>".format(self.id)
import datetime
from project.model import db
from project.model.service.ServiceData import dump_datetime


class WasherData(db.Model):
    __tablename__ = "washer_data"
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255), default="")
    telephoneNumber = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow() + datetime.timedelta(hours=5))
    washer_id = db.Column(db.Integer, db.ForeignKey("washer.id"))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'image': self.image,
            'telephoneNumber': self.telephoneNumber,
            'created': dump_datetime(self.created)
        }
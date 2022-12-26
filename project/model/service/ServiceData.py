import datetime
from project.model import db
from project.utils.Extension import dump_datetime


class ServiceData(db.Model):
    __tablename__ = "service_data"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=(datetime.datetime.utcnow() + datetime.timedelta(hours=5)))
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'price': self.price,
            'duration': self.duration,
            'created': dump_datetime(self.created)
        }
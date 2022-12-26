from project.model import db


class Car(db.Model):
    __tablename__ = "car"
    id = db.Column(db.Integer, primary_key=True)
    carModel = db.Column(db.String(255), default="")
    carNumber = db.Column(db.String(255))
    order = db.relationship("Order", backref="car")
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))

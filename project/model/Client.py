from project.model import db


class Client(db.Model):
    __tablename__ = "client"
    id = db.Column(db.Integer, primary_key=True)
    telephoneNumber = db.Column(db.Integer)
    name = db.Column(db.String(255), default="")
    order = db.relationship("Order", backref="client")
    car = db.relationship("Car", backref="client")

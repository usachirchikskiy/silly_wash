import datetime

from project.model import db


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    isActive = db.Column(db.Boolean,default = True)
    created = db.Column(db.DateTime)
    completed = db.Column(db.DateTime)
    washCompany_id = db.Column(db.Integer, db.ForeignKey("wash_company.id"))
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))

    @property
    def serialize_washer_orders(self):
        return {
            'id': self.id,
            'price': self.price,
            'isActive': self.isActive,
            'created': self.created,
            'completed':self.completed,
            'services':len(self.services),
            'washers': [i.serialize for i in self.washers],
            'carModel': self.car.carModel,
            'carNumber':self.car.carNumber
        }


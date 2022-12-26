from project.model import db


class OrderWasherCrossRef(db.Model):
    __tablename__ = "order_washer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    washer_id = db.Column(db.Integer, db.ForeignKey("washer.id"))
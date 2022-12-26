from project.model import db


class OrderServiceCrossRef(db.Model):
    __tablename__ = "order_service"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    service_id = db.Column(db.Integer, db.ForeignKey("service.id"))
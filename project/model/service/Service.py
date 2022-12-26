from project.model import db


class Service(db.Model):
    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    isDeleted = db.Column(db.Boolean, default = False)
    serviceData = db.relationship("ServiceData", backref="service")
    washCompany_id = db.Column(db.Integer, db.ForeignKey("wash_company.id"))
    order = db.relationship("Order", secondary="order_service", backref='services')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""

        return {
            'id': self.id,
            'title':self.title,
            'isDeleted':self.isDeleted,
            'serviceData': self.serviceData[-1].serialize
        }



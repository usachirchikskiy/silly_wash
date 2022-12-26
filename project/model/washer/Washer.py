from project.model import db


class Washer(db.Model):
    __tablename__ = "washer"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    isDeleted = db.Column(db.Boolean, default=False)
    washerData = db.relationship("WasherData", backref="washer")
    washCompany_id = db.Column(db.Integer, db.ForeignKey("wash_company.id"))
    order = db.relationship("Order", secondary="order_washer", backref='washers')

    @property
    def serialize(self):
        """Return object data in easily serializable format"""

        return {
            'id': self.id,
            'name': self.name,
            'isDeleted': self.isDeleted,
            'washerData': self.washerData[-1].serialize
        }

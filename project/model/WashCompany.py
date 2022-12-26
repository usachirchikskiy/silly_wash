from project.model import db


class WashCompany(db.Model):
    __tablename__ = "wash_company"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    location = db.Column(db.String(255))
    admin = db.relationship("Admin", backref="washCompany")
    service = db.relationship("Service", backref="washCompany")
    order = db.relationship("Order", backref="washCompany")
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.id"))


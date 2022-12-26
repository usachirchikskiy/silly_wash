from project.model import db


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255))
    password = db.Column(db.String(255))
    washCompany_id = db.Column(db.Integer, db.ForeignKey("wash_company.id"))


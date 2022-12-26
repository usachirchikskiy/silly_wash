from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

from project.model.Owner import Owner
from project.model.WashCompany import WashCompany
from project.model.Admin import Admin
from project.model.service.Service import Service
from project.model.service.ServiceData import ServiceData
from project.model.washer.Washer import Washer
from project.model.washer.WasherData import WasherData
from project.model.Car import Car
from project.model.Client import Client
from project.model.cross_ref.OrderServiceCrossRef import OrderServiceCrossRef
from project.model.cross_ref.OrderWasherCrossRef import OrderWasherCrossRef
from project.model.Order import Order

def init_app(app):
    db.init_app(app)
    migrate.init_app(app,db)
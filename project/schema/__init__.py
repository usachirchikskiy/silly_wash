from flask_marshmallow import Marshmallow

ma = Marshmallow()

from project.schema.OwnerSchema import OwnerSchema


def init_app(app):
    ma.init_app(app)

from project.model import Client
from project.schema import ma


class ClientSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    class Meta:
        model = Client

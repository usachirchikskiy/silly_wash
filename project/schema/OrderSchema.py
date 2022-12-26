from project.model import Order
from project.schema import ma
from project.schema.CarSchema import CarSchema
from project.schema.ClientSchema import ClientSchema
from project.schema.ServiceSchema import ServiceSchema
from project.schema.WasherSchema import WasherSchema


class OrderSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    services = ma.Nested(ServiceSchema, many=True)
    washers = ma.Nested(WasherSchema, many=True)
    client = ma.Nested(ClientSchema)
    car = ma.Nested(CarSchema)
    class Meta:
        model = Order

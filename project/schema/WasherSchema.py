from project.model.washer.Washer import Washer
from project.schema import ma


class WasherSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    # order = ma.Nested(OrderSchema,many = True)
    class Meta:
        model = Washer




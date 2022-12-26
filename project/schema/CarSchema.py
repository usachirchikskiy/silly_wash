from project.model import Car
from project.schema import ma


class CarSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    class Meta:
        model = Car

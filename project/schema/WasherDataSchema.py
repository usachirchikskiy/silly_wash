from project.model.washer.WasherData import WasherData
from project.schema import ma


class WasherDataSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    class Meta:
        model = WasherData

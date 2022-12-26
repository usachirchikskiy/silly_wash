from project.model.service.ServiceData import ServiceData
from project.schema import ma


class ServiceDataSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    class Meta:
        model = ServiceData

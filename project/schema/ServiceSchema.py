from project.model.service.Service import Service
from project.schema import ma
from project.schema.ServiceDataSchema import ServiceDataSchema


class ServiceSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    class Meta:
        model = Service

    # serviceData = ma.Nested(ServiceDataSchema,  many=True)



from project.model.Admin import Admin
from project.schema import ma


class AdminSchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    class Meta:
        model = Admin

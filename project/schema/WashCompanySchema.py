from project.model.WashCompany import WashCompany
from project.schema import ma
from project.schema.AdminSchema import AdminSchema


class WashCompanySchema(ma.SQLAlchemyAutoSchema):  # convert DB object to Json
    # admin = ma.Nested(AdminSchema,many = True)

    class Meta:
        model = WashCompany

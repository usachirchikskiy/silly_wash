from project.model.Owner import Owner
from project.schema import ma
# from project.schema.WashCompanySchema import WashCompanySchema


class OwnerSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Owner

    # washCompany = ma.Nested(WashCompanySchema,many = True)

from flask import Blueprint, request, jsonify, Response
from project.mapper.Mapper import body_to_washCompany_entity
from project.model import db, WashCompany
from project.schema.WashCompanySchema import WashCompanySchema

washCompany_bp = Blueprint('washCompany_bp', __name__)
wash_company_schema = WashCompanySchema()


@washCompany_bp.route("/addWashCompany", methods=["POST"])
def add_wash_company():
    try:
        body = request.get_json()
        washCompany = body_to_washCompany_entity(body)
        db.session.add(washCompany)
        db.session.commit()
        return jsonify(wash_company_schema.dump(washCompany))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@washCompany_bp.route("/getWashCompany/<int:id>", methods=["GET"])
def get_wash_company(id):
    try:
        washCompany = WashCompany.query.get(id)
        return jsonify(wash_company_schema.dump(washCompany))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )

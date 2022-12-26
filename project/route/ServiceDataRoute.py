from flask import Blueprint, request, jsonify, Response
from project.mapper.Mapper import body_to_service_data_entity
from project.model import db
from project.model.service.ServiceData import ServiceData
from project.schema.ServiceDataSchema import ServiceDataSchema

service_data_bp = Blueprint('service_data_bp', __name__)
service_data_schema = ServiceDataSchema()


@service_data_bp.route("/addServiceData", methods=["POST"])
def add_service_data():
    try:
        body = request.get_json()
        serviceData = body_to_service_data_entity(body)
        db.session.add(serviceData)
        db.session.commit()
        return jsonify(service_data_schema.dump(serviceData))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@service_data_bp.route("/getServiceData/<int:id>", methods=["GET"])
def service_data(id):
    try:
        serviceData = ServiceData.query.get(id)
        return jsonify(service_data_schema.dump(serviceData))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )

# @service_data_bp.route("/getCurrentServiceData/<int:id>", methods=["GET"])
def current_service_data(id,date):
    try:
        serviceData = ServiceData.query.filter(ServiceData.service_id == id,ServiceData.created<date).order_by(ServiceData.created.desc()).first()
        print(serviceData.created)
        return jsonify(service_data_schema.dump(serviceData))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )
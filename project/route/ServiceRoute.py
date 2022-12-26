from flask import Blueprint, Response, request

from project.mapper.Mapper import body_to_service_entity, body_to_service_data_entity
from project.model import db
from project.model.service.Service import Service
from project.utils.Extension import checkOrdersActive

service_bp = Blueprint('service_bp', __name__)


# service_schema = ServiceSchema()
# services_schema = ServiceSchema(many = True)


@service_bp.route("/addService", methods=["POST"])
def add_service():
    try:
        body = request.get_json()
        service = body_to_service_entity(body)
        db.session.add(service)
        db.session.commit()
        return service.serialize
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@service_bp.route("/updateService/<int:id>", methods=["POST"])
def update_service(id):
    try:
        body = request.get_json()
        service = Service.query.get(id)
        service.title = body['title']
        service_data = body_to_service_data_entity(body)
        db.session.add(service_data)
        db.session.commit()
        return service.serialize
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@service_bp.route("/deleteService/<int:id>", methods=["POST"])
def delete_service(id):
    try:
        service = Service.query.get(id)
        if (checkOrdersActive(service.order)):
            service.isDeleted = True
            db.session.commit()
            return service.serialize
        raise Exception("Order is Active")
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@service_bp.route("/getService/<int:id>", methods=["GET"])
def get_service(id):
    try:
        service = Service.query.get(id)
        return service.serialize
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@service_bp.route("/<int:washCompany_id>/getServices", methods=["GET"])
def get_services(washCompany_id):
    args = request.args
    page = args.get('page')
    try:
        services = Service.query.filter(Service.isDeleted == False, Service.washCompany_id == washCompany_id).order_by(
            Service.title.asc()).paginate(page=int(page), per_page=10, error_out=False)
        return [i.serialize for i in services]
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )

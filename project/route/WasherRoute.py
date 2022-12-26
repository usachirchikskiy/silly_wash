from flask import Blueprint, Response, request, jsonify

from project.mapper.Mapper import body_to_service_entity, body_to_washer_entity, body_to_washer_data_entity
from project.model import db
from project.model.washer.Washer import Washer
from project.schema.WasherSchema import WasherSchema
from project.utils.Extension import checkOrdersActive

washer_bp = Blueprint('washer_bp', __name__)
# washer_schema = WasherSchema()


# washers_schema = WasherSchema(many = True)


@washer_bp.route("/addWasher", methods=["POST"])
def add_washer():
    try:
        body = request.get_json()
        washer = body_to_washer_entity(body)
        db.session.add(washer)
        db.session.commit()
        return washer.serialize
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@washer_bp.route("/updateWasher/<int:id>", methods=["POST"])
def update_washer(id):
    try:
        body = request.get_json()
        washer = Washer.query.get(id)
        washer.name = body['title']
        washer_data = body_to_washer_data_entity(body)
        db.session.add(washer_data)
        db.session.commit()
        return washer.serialize
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@washer_bp.route("/getWasher/<int:id>", methods=["GET"])
def get_service(id):
    try:
        washer = Washer.query.get(id)
        return washer.serialize
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@washer_bp.route("/deleteWasher/<int:id>", methods=["POST"])
def delete_service(id):
    try:
        washer = Washer.query.get(id)
        if (checkOrdersActive(washer.order)):
            washer.isDeleted = True
            db.session.commit()
            return washer.serialize
        raise Exception("Order is Active")
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@washer_bp.route("/<int:washCompany_id>/getWashers", methods=["GET"])
def get_services(washCompany_id):
    args = request.args
    page = args.get('page')
    try:
        washers = Washer.query.filter(Washer.washCompany_id == washCompany_id, Washer.isDeleted == False).order_by(
            Washer.name.asc()).paginate(page=int(page), per_page=10, error_out=False)
        return [i.serialize for i in washers]
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )

@washer_bp.route("/getWasherOrders/<int:id>", methods=["GET"])
def get_washer_orders(id):
    orders = Washer.query.get(id).order
    return [order.serialize_washer_orders for order in orders]

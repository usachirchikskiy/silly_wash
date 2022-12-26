from flask import Blueprint, request, jsonify, Response
from project.mapper.Mapper import body_to_service_data_entity, body_to_washer_data_entity
from project.model import db
from project.model.washer.WasherData import WasherData
from project.schema.WasherDataSchema import WasherDataSchema

washer_data_bp = Blueprint('washer_data_bp', __name__)
washer_data_schema = WasherDataSchema()


@washer_data_bp.route("/addWasherData", methods=["POST"])
def add_service_data():
    try:
        body = request.get_json()
        washerData = body_to_washer_data_entity(body)
        db.session.add(washerData)
        db.session.commit()
        return jsonify(washer_data_schema.dump(washerData))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@washer_data_bp.route("/getWasherData/<int:id>", methods=["GET"])
def service_data(id):
    try:
        washerData = WasherData.query.get(id)
        return jsonify(washer_data_schema.dump(washerData))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )

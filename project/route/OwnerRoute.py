from flask import Blueprint, Response, request, jsonify

from project.mapper.Mapper import body_to_owner_entity
from project.model import db, Owner
from project.schema.OwnerSchema import OwnerSchema

owner_bp = Blueprint('owner_bp', __name__)
owner_schema = OwnerSchema()


@owner_bp.route("/addOwner", methods=["POST"])
def add_owner():
    try:
        body = request.get_json()
        owner = body_to_owner_entity(body)
        db.session.add(owner)
        db.session.commit()
        return jsonify(owner_schema.dump(owner))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@owner_bp.route("/getOwner/<int:id>", methods=["GET"])
def get_owner(id):
    try:
        owner = Owner.query.get(id)
        return jsonify(owner_schema.dump(owner))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )

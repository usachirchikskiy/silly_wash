from flask import Blueprint, jsonify, Response
from flask import request
from project.mapper.Mapper import body_to_admin_entity
from project.model import db, Admin
from project.schema.AdminSchema import AdminSchema

admin_bp = Blueprint('admin_bp', __name__)
admin_schema = AdminSchema()


@admin_bp.route("/addAdmin", methods=["POST"])
def add_admin():
    try:
        body = request.get_json()
        admin = body_to_admin_entity(body)
        db.session.add(admin)
        db.session.commit()
        return jsonify(admin_schema.dump(admin))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@admin_bp.route("/getAdmin/<int:id>", methods=["GET"])
def get_admin(id):
    try:
        admin = Admin.query.get(id)
        return jsonify(admin_schema.dump(admin))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )

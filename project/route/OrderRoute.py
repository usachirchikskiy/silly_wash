import datetime

from flask import Blueprint, Response, request, jsonify

from project.model import db, Owner, Client, Car, Order
from project.model.service.Service import Service
from project.model.washer.Washer import Washer
from project.route.ServiceDataRoute import current_service_data
from project.schema.OrderSchema import OrderSchema

order_bp = Blueprint('order_bp', __name__)
order_schema = OrderSchema()


@order_bp.route("/addOrder", methods=["POST"])
def add_order():
    try:
        body = request.get_json()
        telephoneNumber = body['telephoneNumber']
        name = body['name']
        carModel = body['carModel']
        carNumber = body['carNumber']
        service_ids = body['services']
        washer_ids = body['washers']
        washCompany_id = body['washCompany_id']
        price = getPrice(service_ids)
        duration = getDuration(service_ids)
        client_id = createClientOrNot(telephoneNumber, name)
        car_id = createCarOrNot(carModel, carNumber, client_id)

        created = datetime.datetime.utcnow() + datetime.timedelta(hours=5)
        completed = created + datetime.timedelta(minutes=duration)

        order = Order(price=price, washCompany_id=washCompany_id, client_id=client_id, car_id=car_id, created = created, completed = completed)
        print(order.created)
        print(order.completed)
        addServicesToOrder(order,service_ids)
        addWashersToOrder(order,washer_ids)
        db.session.add(order)
        db.session.commit()
        current_service_data(service_ids[0],order.created)
        return jsonify(order_schema.dump(order))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@order_bp.route("/getOrder/<int:id>", methods=["GET"])
def get_order(id):
    try:
        order = Order.query.get(id)
        current_service_data(1, order.created)
        return jsonify(order_schema.dump(order))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )


@order_bp.route("/completeOrder/<int:id>", methods=["GET"])
def complete_order(id):
    try:
        order = Order.query.get(id)
        order.isActive = False
        db.session.commit()
        return jsonify(order_schema.dump(order))
    except Exception as ex:
        return Response(
            str(ex),
            status=400,
        )



def createClientOrNot(telephoneNumber, name):
    try:
        client = Client.query.filter(Client.telephoneNumber == telephoneNumber, Client.name == name).first()
        return client.id
    except Exception as ex:
        new_client = Client(telephoneNumber=telephoneNumber, name=name)
        db.session.add(new_client)
        db.session.commit()
        return new_client.id


def createCarOrNot(carModel, carNumber, client_id):
    try:
        car = Car.query.filter(Car.carModel == carModel, Car.carNumber == carNumber, Car.client_id == client_id).first()
        return car.id
    except Exception as ex:
        new_car = Car(carModel=carModel, carNumber=carNumber, client_id=client_id)
        db.session.add(new_car)
        db.session.commit()
        return new_car.id


def getPrice(service_ids):
    price = 0
    for id in service_ids:
        price = price + Service.query.get(id).serviceData[-1].price
    return price

def getDuration(service_ids):
    duration = 0
    for id in service_ids:
        duration = duration + Service.query.get(id).serviceData[-1].duration
    return duration

def addServicesToOrder(order,service_ids):
    for id in service_ids:
        service = Service.query.get(id)
        order.services.append(service)


def addWashersToOrder(order,washer_ids):
    for id in washer_ids:
        washer = Washer.query.get(id)
        order.washers.append(washer)
#
# @order_bp.route("/addWashCompany", methods=["POST"])
# def add_wash_company():
#     try:
#         body = request.get_json()
#         washCompany = body_to_washCompany_entity(body)
#         db.session.add(washCompany)
#         db.session.commit()
#         return jsonify(wash_company_schema.dump(washCompany))
#     except Exception as ex:
#         return Response(
#             str(ex),
#             status=400,
#         )
#
#
# @order_bp.route("/getWashCompany/<int:id>", methods=["GET"])
# def get_wash_company(id):
#     try:
#         washCompany = WashCompany.query.get(id)
#         return jsonify(wash_company_schema.dump(washCompany))
#     except Exception as ex:
#         return Response(
#             str(ex),
#             status=400,
#         )
#
#
# @order_bp.route("/addAdmin", methods=["POST"])
# def add_admin():
#     try:
#         body = request.get_json()
#         admin = body_to_admin_entity(body)
#         db.session.add(admin)
#         db.session.commit()
#         return jsonify(admin_schema.dump(admin))
#     except Exception as ex:
#         return Response(
#             str(ex),
#             status=400,
#         )
#
# @order_bp.route("/getAdmin/<int:id>", methods=["GET"])
# def get_admin(id):
#     try:
#         admin = Admin.query.get(id)
#         return jsonify(admin_schema.dump(admin))
#     except Exception as ex:
#         return Response(
#             str(ex),
#             status=400,
#         )

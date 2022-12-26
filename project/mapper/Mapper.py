from project.model import Order
from project.model.Admin import Admin
from project.model.Owner import Owner
from project.model.WashCompany import WashCompany
from project.model.service.Service import Service
from project.model.service.ServiceData import ServiceData
from project.model.washer.Washer import Washer
from project.model.washer.WasherData import WasherData


def body_to_owner_entity(body):
    return Owner(name=body['name'], password=body['password'])


def body_to_washCompany_entity(body):
    return WashCompany(title=body['title'], location=body['location'], owner_id=body["owner_id"])


def body_to_admin_entity(body):
    return Admin(login=body['login'], password=body['password'], washCompany_id=body["washCompany_id"])

def body_to_order_entity(body):
    return Order()

def body_to_service_entity(body):
    return Service(title=body['title'], washCompany_id=body["washCompany_id"])


def body_to_service_data_entity(body):
    return ServiceData(price=body['price'], duration=body['duration'], service_id=body['service_id'])


def body_to_washer_entity(body):
    return Washer(name=body['name'], washCompany_id=body["washCompany_id"])


def body_to_washer_data_entity(body):
    if 'image' not in body:
        return WasherData(telephoneNumber=body['telephoneNumber'], washer_id=body['washer_id'])
    return WasherData(image=body['image'], telephoneNumber=body['telephoneNumber'], washer_id=body['washer_id'])

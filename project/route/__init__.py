from .OwnerRoute import owner_bp
from .WashCompanyRoute import washCompany_bp
from .AdminRoute import admin_bp
from .OrderRoute import order_bp
from .ServiceRoute import service_bp
from .ServiceDataRoute import service_data_bp
from .WasherRoute import washer_bp
from .WasherDataRoute import washer_data_bp


def init_app(app):
    app.register_blueprint(owner_bp)
    app.register_blueprint(washCompany_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(service_data_bp)
    app.register_blueprint(washer_bp)
    app.register_blueprint(washer_data_bp)
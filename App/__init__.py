from flask import Flask, redirect
import flask_wtf


def logistics():
    app = Flask("Logistics")  # Creating Flask App
    app.config['SECRET_KEY'] = "Testing"  # Secret Key (temporary)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    csrf = flask_wtf.CSRFProtect()  # To protect from CSRF attacks
    csrf.init_app(app)

    from . import shipment, inventory, db
    app.register_blueprint(shipment.shipment)
    app.register_blueprint(inventory.inventory)

    db.db.init_app(app)
    with app.app_context():
        db.db.create_all()

    @app.route("/")  # Keeping the "/" open for other function in case of future integration in another app
    def main():
        return redirect("/inventory/")

    return app

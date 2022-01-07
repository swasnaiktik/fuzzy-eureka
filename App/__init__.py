import os

from flask import Flask, redirect
import flask_wtf

def logistics():
    app = Flask("Logistics")
    app.config['SECRET_KEY'] = "Testing"

    csrf = flask_wtf.CSRFProtect()
    csrf.init_app(app)

    from . import shipment, inventory, db
    app.register_blueprint(shipment.shipment)
    app.register_blueprint(inventory.inventory)

    db.db.init_app(app)
    with app.app_context():
        db.db.create_all()

    @app.route("/")
    def main():
        return redirect("/inventory/")

    return app

from flask import Blueprint, render_template, request, redirect, flash
from .db import db, InventoryItem, Shipment, ShipmentItems
shipment = Blueprint("shipment", __name__, template_folder='templates', static_folder='static', url_prefix='/shipment')


@shipment.route("/", methods=['GET', 'POST'])
def shipmentLanding():
    if request.method == 'GET':
        inventoryItems = InventoryItem.query.all() or []
        shipmentList = Shipment.query.all()
        return render_template("shipment.html", itemList=inventoryItems, shipmentList=shipmentList)
    else:
        try:
            shipment = Shipment(name=request.form['Name'])
            items = InventoryItem.query.all()
            for item in items:
                item_quantity = request.form[item.name]
                if item_quantity:
                    ship = ShipmentItems(item=item, quantity=item_quantity)
                    shipment.items.append(ship)
                    db.session.add(ship)
            db.session.add(shipment)
            db.session.commit()
            flash("Successfully to Created a Shipment")
        except:
            flash("Failed to Create a Shipment")

        return redirect('/shipment/')

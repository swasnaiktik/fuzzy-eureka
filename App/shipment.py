from flask import Blueprint, render_template, request, redirect, flash
from .db import db, InventoryItem, Shipment, ShipmentItems
from .helper import checkQuantity

shipment = Blueprint("shipment", __name__, template_folder='templates', static_folder='static', url_prefix='/shipment')


# GET:  /shipment/ provided HTML of the shipment html page
# POST: /shipment/ creates an Shipment according to the provided data and updates the quantity of items
@shipment.route("/", methods=['GET', 'POST'])
def shipmentLanding():
    if request.method == 'GET':
        inventoryItems = InventoryItem.query.all() or []
        shipmentList = Shipment.query.all()
        return render_template("shipment.html", itemList=inventoryItems, shipmentList=shipmentList)
    else:
        try:
            shipment = Shipment()
            shipment.updateShipment(name=request.form['name'], description=request.form['description'])
            items = InventoryItem.query.all()
            emptyShipment = True
            for item in items:
                shipmentItemQuantity = int(request.form[item.name])
                if shipmentItemQuantity:
                    checkQuantity(shipmentItemQuantity, item.quantity)
                    emptyShipment = False
                    item.quantity -= shipmentItemQuantity
                    ship = ShipmentItems()
                    ship.updateShipmentItem(name=item.name, item=item, quantity=shipmentItemQuantity)
                    shipment.items.append(ship)
                    db.session.add(ship)
            if emptyShipment:
                raise RuntimeError
            db.session.add(shipment)
            db.session.commit()
            flash("Successfully to Created a Shipment")
        except:
            flash("Failed to Create a Shipment")
        return redirect('/shipment/')

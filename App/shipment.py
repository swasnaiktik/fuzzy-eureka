from flask import Blueprint, render_template, request, redirect
from .db import InventoryItem
shipment = Blueprint("shipment", __name__, template_folder='templates', static_folder='static', url_prefix='/shipment')


@shipment.route("/", methods=['GET', 'POST'])
def shipmentLanding():
    if request.method == 'GET':
        inventoryItems = InventoryItem.query.all() or []
        return render_template("shipment.html", itemList=inventoryItems)
    else:
        return redirect('/shipment/')

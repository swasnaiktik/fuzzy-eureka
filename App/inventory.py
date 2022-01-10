from flask import Blueprint, render_template, request, redirect, flash
from .db import db, InventoryItem, ShipmentItems

inventory = Blueprint("inventory", __name__, template_folder='templates', static_folder='static', url_prefix='/inventory')


@inventory.route("/", methods=['GET', 'POST'])
def inventoryLanding():
    if request.method == 'GET':
        inventoryItems = InventoryItem.query.all() or []
        return render_template("inventory.html", inventoryItems=inventoryItems)
    else:
        name, quantity, description = request.form["name"], request.form["quantity"], request.form["description"]
        try:
            newInventoryItem = InventoryItem()
            newInventoryItem.updateItem(name, quantity, description)
            db.session.add(newInventoryItem)
            db.session.commit()
            flash("New Inventory Item Created!")
        except:
            flash("Error in Item Creation")
        return redirect('/inventory/')


@inventory.route("/<item>/<action>")
def actions(item, action):
    try:
        item = InventoryItem.query.filter_by(name=item)
        if action == "increase":
            item.first().quantity += 1
        elif action == "decrease":
            item = item.first()
            item.quantity = max(item.quantity - 1, 0)
        elif action == "delete":
            item.delete()
        else:
            raise RuntimeError
        db.session.commit()
        return "Success"
    except:
        return "Failed"


@inventory.route("/editForm/<item>", methods=['GET', 'POST'])
def editItemForm(item):
    try:
        item = InventoryItem.query.filter_by(name=item).first()
        if request.method == 'GET':
            return render_template("editItemForm.html", item=item)
        else:
            name, quantity, description = request.form["edit-name"], request.form["edit-quantity"], request.form["edit-description"]
            if item.name != name:
                shipmentItems = ShipmentItems.query.filter_by(name=item.name).all()
                for shipmentItem in shipmentItems:
                    shipmentItem.updateShipmentItem(name=name)
            item.updateItem(name, quantity, description)
            db.session.commit()
    except:
        flash('Failed Something wrong with the passed item')
    return redirect('/inventory/')

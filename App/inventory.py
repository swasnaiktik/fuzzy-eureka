from flask import Blueprint, render_template, request, redirect, flash
from .db import db, InventoryItem

inventory = Blueprint("inventory", __name__, template_folder='templates', static_folder='static',
                      url_prefix='/inventory')


@inventory.route("/", methods=['GET', 'POST'])
def inventoryLanding():
    if request.method == 'GET':
        inventoryItems = InventoryItem.query.all() or []
        return render_template("inventory.html", inventoryItems=inventoryItems)
    else:
        name, quantity = request.form["Name"], request.form["Quantity"]
        try:
            newInventoryItem = InventoryItem(name=name, quantity=quantity)
            db.session.add(newInventoryItem)
            db.session.commit()
            flash("New Inventory Item Created!")
        except:
            flash("Error in Item Creation")
        return redirect('/inventory/')

@inventory.route("/<item>/<action>")
def actions(item, action):
    try:
        item = InventoryItem.query.filter_by(name=item).first()
        if action == "increase":
            item.quantity += 1
        elif action == "decrease":
            item.quantity = max(item.quantity - 1, 0)
        else:
            raise RuntimeError
        db.session.commit()
        return "Success"
    except:
        return "Failed"


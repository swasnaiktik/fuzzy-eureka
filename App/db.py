from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .helper import validateStr


db = SQLAlchemy()


class InventoryItem(db.Model):    # Table to store data of an Inventory Item
    __tablename__ = 'InventoryItem'
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    name = db.Column(db.String(100), unique=True, nullable=False)  # String name of an Item
    quantity = db.Column(db.Integer, nullable=False)  # Integer quantity of an Item
    description = db.Column(db.Text, nullable=False)  # String (long) description of an Item
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # date of creation

    def updateItem(self, name=None, quantity=None, description=None):  # Function to add or update value of an instance with validation
        if name:
            self.name = validateStr(str(name))
        if quantity:
            self.quantity = int(quantity)
        if description:
            self.description = validateStr(str(description))

    def __repr__(self):
        return '<InventoryItem %r>' % self.name


class Shipment(db.Model):  # Table to store data of a Shipment
    __tablename__ = 'Shipment'
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), unique=True, nullable=False)  # String name of a Shipment
    items = db.relationship('ShipmentItems', backref='Shipment')  # One to Many elation ship to ShipmentItems
    description = db.Column(db.Text, nullable=False)  # String (long) description of a Shipment
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Time of creation

    def updateShipment(self, name=None, description=None):  # Function to add or update value of an instance with validation
        if name:
            self.name = validateStr(str(name))
        if description:
            self.description = validateStr(str(description))

    def __repr__(self):
        return '<Shipment %r>' % self.name


class ShipmentItems(db.Model):  # Table to store data of items from an Shipment
    __tablename__ = 'ShipmentItems'
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    shipment_id = db.Column(db.Integer, db.ForeignKey(Shipment.id))  # Shipment id to which this item belongs tp
    name = db.Column(db.String(100), unique=True, nullable=False)  # Name of the item (stored in case item is deleted from inventory)
    item_id = db.Column(db.Integer, db.ForeignKey(InventoryItem.id))  # Item Id
    item = db.relationship(InventoryItem)  # Relationship from this item to the actual item in the InventoryItem Table
    quantity = db.Column(db.Integer, nullable=False)  # Quantity of the item in the Shipment

    def updateShipmentItem(self, name=None, item=None, quantity=None):  # Function to add or update value of an instance with validation
        if name:
            self.name = validateStr(str(name))
        if item:
            self.item = item
        if quantity:
            self.quantity = int(quantity)

    def __repr__(self):
        return '<ShipmentItems %r>' % self.id
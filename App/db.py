from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .helper import validateStr


db = SQLAlchemy()


class InventoryItem(db.Model):
    __tablename__ = 'InventoryItem'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def updateItem(self, name=None, quantity=None, description=None):
        if name:
            self.name = validateStr(str(name))
        if quantity:
            self.quantity = int(quantity)
        if description:
            self.description = validateStr(str(description))

    def __repr__(self):
        return '<InventoryItem %r>' % self.name


class Shipment(db.Model):
    __tablename__ = 'Shipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    items = db.relationship('ShipmentItems', backref='Shipment')
    description = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def updateShipment(self, name=None, description=None):
        if name:
            self.name = validateStr(str(name))
        if description:
            self.description = validateStr(str(description))

    def __repr__(self):
        return '<Shipment %r>' % self.name


class ShipmentItems(db.Model):
    __tablename__ = 'ShipmentItems'
    id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey(Shipment.id))
    name = db.Column(db.String(100), unique=True, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey(InventoryItem.id))
    item = db.relationship(InventoryItem)
    quantity = db.Column(db.Integer, nullable=False)

    def updateShipmentItem(self, name=None, item=None, quantity=None):
        if name:
            self.name = validateStr(str(name))
        if item:
            self.item = item
        if quantity:
            self.quantity = int(quantity)

    def __repr__(self):
        return '<ShipmentItems %r>' % self.id
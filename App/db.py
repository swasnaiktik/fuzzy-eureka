from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class InventoryItem(db.Model):
    __tablename__ = 'InventoryItem'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<InventoryItem %r>' % self.name


class Shipment(db.Model):
    __tablename__ = 'Shipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    items = db.relationship('ShipmentItems', backref='Shipment')
    status = db.Column(db.String(100), nullable=False, default="Not Shipped")
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shipped = db.Column(db.DateTime)

    def __repr__(self):
        return '<Shipment %r>' % self.name


class ShipmentItems(db.Model):
    __tablename__ = 'ShipmentItems'
    id = db.Column(db.Integer, primary_key=True)
    shipment_id = db.Column(db.Integer, db.ForeignKey(Shipment.id))
    item_id = db.Column(db.Integer, db.ForeignKey(InventoryItem.id))
    item = db.relationship(InventoryItem)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<ShipmentItems %r>' % self.id
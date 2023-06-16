from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config["SQLAlCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "db.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Initialize db
db = SQLAlchemy(app)

#Initialize ma
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

# Product Schema
class ProductSchema(ma.Schema):
    # Fields that we want to show
    class Meta:
        fields = ("id", "name", "description", "price", "quantity")

# Initialize ProductSchema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)

# Run Server
if __name__ == "__main__":
    app.run(debug=True)

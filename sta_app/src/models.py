import datetime
from flask_sqlalchemy import SQLAlchemy

# DB adapter object with sqlalchemy class
db = SQLAlchemy()

# Create Product subclass of base db.Model
class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    qty = db.Column(db.Integer, nullable=False)
    cat_id = db.Column(db.Integer, db.ForeignKey('categories.cat_id'), nullable=False)
    color = db.Column(db.String(128), nullable=False)
    material = db.Column(db.String(128))
    style = db.Column(db.String(128))

    def __init__(self, qty: int, cat_id: int, color: str):
        self.qty = qty
        self.cat_id = cat_id
        self.color = color 

    def serialize(self):
        return {
            'product_id': self.product_id,
            'qty': self.qty,
            'cat_id': self.cat_id,
            'color': self.color,
            'material': self.material,
            'style': self.style
        }



# Create Category subclass of base db.Model
class Category(db.Model):
    __tablename__= 'categories'
    cat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

    def __init__(self, name: str):
        self.name = name

    def serialize(self):
        return {
            'cat_id': self.cat_id,
            'name': self.name
        }

# Create order_product reference table
orders_products_table = db.Table(
    'orders_products',
    db.Column(
        'order_id', db.Integer,
        db.ForeignKey('orders.order_id'),
        primary_key=True
    ),
    db.Column(
        'cust_id', db.Integer,
        db.ForeignKey('customers.cust_id'),
        primary_key=True
    ),
    db.Column(
        'qty', db.Integer,
        nullable=False
    ),
    db.Column(
        'price', db.Float,
        nullable=False
    )
        
)

# Create Order subclass of base db.Model
class Order(db.Model):
    __tablename__= 'orders'
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customers.cust_id'), nullable=False)
    total = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

# Create Customer subclass of base db.Model
class Customer(db.Model):
    __tablename__= 'customers' 
    cust_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True)



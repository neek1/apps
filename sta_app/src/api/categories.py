from flask import Blueprint, jsonify, abort, request 
from ..models import Category, Product, db

bp = Blueprint('categories', __name__, url_prefix='/categories')

@bp.route('', methods=['GET'])  # Decorator takes prefix URL and GET method
def index():
    categories = Category.query.all()  # ORM Select * query
    result = []
    for c in categories:
        result.append(c.serialize())
    return jsonify(result)
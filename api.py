from flask import Blueprint, jsonify, make_response
from models import db

api = Blueprint('api', __name__)
@api.route('/index', methods=['GET'])
def index(): return make_response(jsonify('Comming soon'), 200)

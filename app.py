import os
from flask import Flask, send_from_directory
from models import db
from shop import shop
from api import api

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.update({'SECRET_KEY': 'secret_key','SQLALCHEMY_DATABASE_URI': f'sqlite:///{basedir}/app.db'})
db.init_app(app)
with app.app_context(): db.create_all()

app.register_blueprint(shop, url_prefix='/shop')
app.register_blueprint(api, url_prefix='/api')

@app.route('/', methods=['GET'])
def hello(): return 'hello'

@app.route('/uploads/<filename>')
def uploads(filename): return send_from_directory('uploads', filename)

if __name__ == '__main__': app.run(host = '0.0.0.0', port = 5000, debug=True)

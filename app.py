from flask import Flask
from flask_restful import Api
from config import mysqlConfig
from api.controllers.PingController import PingController
from api.controllers.PositionController import PositionController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = mysqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


with app.app_context():
    from db import db
    db.init_app(app)
    db.create_all()


api = Api(app)
api.add_resource(PingController, '/ping')
api.add_resource(PositionController, '/api/position')

# Setup the Flask-JWT-Extended extension
# app.config["JWT_SECRET_KEY"] = "Dese.Decent.Pups.BOOYO0OST"  # Change this!
# jwt = JWTManager()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


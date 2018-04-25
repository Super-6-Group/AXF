

from flask import Flask

from App.apis import init_api
from App.ext import init_ext



def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = "110"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/FlaskDay05REST"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_ext(app)

    init_api(app)

    return app
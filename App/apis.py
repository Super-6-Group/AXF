from flask import Blueprint
from flask_restful import Resource, Api

from App.models import HomeBanner

api = Api()
def init_api(app):
    api.init_app(app=app)



class HomeResource(Resource):
    def get(self):
        homebanners = HomeBanner.query.all()


        return {'msg':'ok'}

api.add_resource(HomeResource,'/home/')
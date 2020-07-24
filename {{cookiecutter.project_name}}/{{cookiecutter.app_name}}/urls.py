# 此模块是为了便于管理url 因此从views中引入api, blueprint，views

from {{cookiecutter.app_name}}.api.views import api, blueprint
from {{cookiecutter.app_name}}.api.views import ResfulHelloViews
from {{cookiecutter.app_name}}.extensions import apispec
from flask import current_app

api.add_resource(ResfulHelloViews, '/hello/<string:name>')

@blueprint.before_app_first_request
def register_views():
    apispec.spec.path(view=ResfulHelloViews, app=current_app)
#  api 视图类
from flask import Blueprint, render_template, jsonify , current_app as app
from flask_restful import Api, Resource, reqparse

#  导入工具类
from {{cookiecutter.app_name}}.utils import removeNoneKey
from pubCode.pubUtils.msgBuilder import MsgBuilder

blueprint = Blueprint(
    'api', __name__,
    url_prefix='/{{cookiecutter.project_name}}/api',
    static_folder='../../Static',
    static_url_path='/static')

api = Api(blueprint)

@blueprint.route('/hello')
def hello():
    return jsonify({
        'code': '000000',
        'succeed': True,
        'message': 'Hello World!!!'
    })

class ResfulHelloViews(Resource):

    def get(self, name):
        return jsonify({
            'code': '000000',
            'succeed': True,
            'message': f'Hello {name}!!!'
        })




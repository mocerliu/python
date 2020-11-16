from flask import Flask, jsonify, abort, make_response, request, Blueprint, Response
from api import app

from functools import wraps
from api.database import db_session, Base, init_db
from api.models import User, TbAccount, Student

main_routes = Blueprint('main', __name__)
# init_db()

tb_user = 'tb_accounts'


@main_routes.app_errorhandler(404)
def page_not_found(e):
    # if request.path.startswith('/api'):
    #     return jsonify({'message':'错误的API请求!'}), 404
    # return render_template("404.html")
    # res =
    # return Response(jsonify({"status": 404, "message": "404错误,找不到对应router"}), mimetype='application/json')
    return jsonify({"message": "no data."}), 404


@main_routes .route('/test', endpoint="test",  methods=['GET'])
def test():
    # return 'Hello, World!'
    return jsonify({"code": 0, "msg": "hello"}), 200

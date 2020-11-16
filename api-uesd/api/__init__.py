
from flask import Flask, jsonify, abort, make_response, request
# from include import route
# from .database import db_session
# from .database import init_db

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# CORS(app, supports_credentials=True)

def after_request(response):
   response.headers['Access-Control-Allow-Origin'] = '*'
   response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
   response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
   return response

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.after_request(after_request)

    # DBSESSION CONFIG
    from api.database import db_session,init_db
    init_db(app)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()


    # Load blueprints
    from api.routers import main_routes
    app.register_blueprint(main_routes) 
    
    return app

    



# 底部导入
# import studentMangerWeb.api
from api import models


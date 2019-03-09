# __init__.py file required to make python treat the directories as containing packages
# executes initialization code for the package
from flask import Flask

from flask_mongoengine import MongoEngine

mongo = MongoEngine()


# flask application factory method
def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    mongo.init_app(app)

    from .group import create_module as group_create_module
    from .main import create_module as main_create_module
    group_create_module(app)
    main_create_module(app)

    return app



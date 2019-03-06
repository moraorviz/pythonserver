from flask import Blueprint

group_blueprint = Blueprint(
    'group',
    __name__,
    url_prefix="/group"
)


@group_blueprint.route('/')
def home():
    return 'Welcome home!'

from .models import mongo, Group, Meet
import sys

from flask import Blueprint, redirect, url_for, current_app

group_blueprint = Blueprint(
    'group',
    __name__,
    url_prefix="/group"
)


# TODO implement shortest distance algorithm
def groups_data():

    meets = Meet.objects

    for meet in meets:
        print(meet.group.groupLon, file=sys.stdout)

    total = meets.count()
    return 'En total hay' + str(total) + 'meetings'


@group_blueprint.route('/')
def home():
    return 'Welcome home!'


@group_blueprint.route('/all', methods=['GET'])
def all_groups():
    return groups_data()


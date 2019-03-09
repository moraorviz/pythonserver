from .models import Meet
import sys

from flask import Blueprint, request

group_blueprint = Blueprint(
    'group',
    __name__,
    url_prefix="/group"
)


# TODO complete method
# Method for choosing the system reference in the coordinates origin (0,0)
# Applicable in the first place to the group's position vectors before calculating the distance to given P
# Uses lambda function
def offset(origin, groups):

    for i in range(len(groups)):
        groups[i][1] -= origin[1]
        groups[i][2] -= origin[2]

    return groups


# TODO implement shortest distance algorithm
def calculate_closest(origin, groups, num):

    groups = offset(groups, origin)
    groups.sort(key=lambda d: d[1]**2 + d[2]**2)

    return groups[:num]


@group_blueprint.route('near_test', methods=['GET'])
def test_parameters():

    lat = request.args.get("lat")
    return '''<h1>The lat value is: {}</h1>'''.format(lat)


@group_blueprint.route('/near', methods=['GET'])
def get_closest():

    origin = [0, request.args.get('lat'), request.args.get('lon')]
    num = 10;
    groups = list()
    meets = Meet.objects
    for meet in meets:

        groups.append(meet.group)

    return calculate_closest(origin, groups, num)


def groups_data():

    meets = Meet.objects
    for meet in meets:

        print(meet.group.groupLon, file=sys.stdout)

    total = meets.count()
    return 'En total hay ' + str(total) + ' meetings'


@group_blueprint.route('/')
def home():
    return 'Welcome home!'


@group_blueprint.route('/all', methods=['GET'])
def all_groups():
    return groups_data()


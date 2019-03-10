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
        groups[i][1] -= origin[0][1]
        groups[i][2] -= origin[0][2]

    return groups


# TODO implement shortest distance algorithm
def calculate_closest(origin, groups, num):

    groups = offset(origin, groups)
    groups.sort(key=lambda d: d[1]**2 + d[2]**2)

    return groups[:num].__repr__()


@group_blueprint.route('/near_test', methods=['GET'])
def test_parameters():

    lon = request.args.get("lon")
    lat = request.args.get("lat")
    return '''<h1>The lon value is: {}</h1>'''.format(lon) + '''<h1>The lat value is: {}</h1>'''.format(lat)


@group_blueprint.route('/near', methods=['GET'])
def get_closest():

    origin = [[0, float(request.args.get('lon')), float(request.args.get('lat'))]]
    num = 20000;
    groups = list()
    meets = Meet.objects
    for meet in meets:

        group = [meet.group.groupId, float(meet.group.groupLon), float(meet.group.groupLat)]
        groups.append(group)

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


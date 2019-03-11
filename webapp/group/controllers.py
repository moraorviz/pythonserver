from .models import Meet
import sys, datetime, requests

from flask import Blueprint, request

group_blueprint = Blueprint(
    'group',
    __name__,
    url_prefix="/group"
)


def offset(origin, groups):

    for i in range(len(groups)):
        groups[i][1] -= origin[0][1]
        groups[i][2] -= origin[0][2]

    return groups


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


@group_blueprint.route("/topCities", methods=['GET'])
def get_top_cities():

    date_iso = request.args.get('date')
    date_add_hour = str(date_iso) + '000001'
    date = datetime.datetime.strptime(date_add_hour, "%Y%m%d%H%M%S")
    epoch = date.utcfromtimestamp(0)
    date_ms = unix_time_millis(date, epoch)
    r = requests.get("http://127.0.0.1:8080/meet/" + str(date_ms))

    cities = {}
    meets = Meet.objects

    for meet in meets:

            if (meet.mTime > date_ms) and (meet.mTime < date_ms + 86400000):
                if meet.group.groupCity in cities:
                    cities[meet.group.groupCity] =

    return ''


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


def unix_time_millis(dt, epoch):
    return int((dt - epoch).total_seconds() * 1000)

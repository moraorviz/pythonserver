from .. import mongo


class Group(mongo.EmbeddedDocument):
    groupId = mongo.IntField(required=True, db_field="groupId")
    groupCity = mongo.StringField(db_field="groupCity")
    groupLon = mongo.FloatField(required=True, db_field="groupLon")
    groupLat = mongo.FloatField(required=True, db_field="groupLat")

    def __repr__(self):
        return {'id': self.groupId, 'groupLon': self.groupLon, 'groupLat': self.groupLat}


class Meet(mongo.Document):
    meta = {'collection': 'meetRepository'}
    objectId = mongo.IntField(requred=True, db_field="_id")
    id = mongo.IntField(required=True, db_field="rsvpId")
    mTime = mongo.IntField(required=True, db_field="mTime")
    guests = mongo.IntField(required=True, db_field="guests")
    group = mongo.EmbeddedDocumentField(Group, db_field="group")
    _class=mongo.StringField(required=True)

    def __repr__(self):
        return "<Meet '{}'".format(self.id)


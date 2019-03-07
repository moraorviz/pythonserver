from .. import mongo


class Group(mongo.EmbeddedDocument):
    id = mongo.IntField(required=True, db_field="_id")
    groupLon = mongo.FloatField(required=True, db_field="groupLon")
    groupLat = mongo.FloatField(required=True, db_field="groupLat")

    def __repr__(self):
        return "<Group '{}'>".format(self.id)


class Meet(mongo.Document):
    meta = {'collection': 'meetRepository'}
    id = mongo.IntField(required=True, db_field="_id")
    group = mongo.EmbeddedDocumentField(Group, db_field="group")
    _class=mongo.StringField(required=True)

    def __repr__(self):
        return "<Meet '{}'".format(self.id)


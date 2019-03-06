from .. import mongo

class Group(mongo.EmbeddedDocument):
    id = mongo.IntField(required=True)
    groupLon = mongo.FloatField(required=True)
    groupLat = mongo.FloatField(required=True)

    def __repr__(self):
        return "<Group '{}'>".format(self.id)


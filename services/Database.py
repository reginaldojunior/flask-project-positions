import pymongo
import os


class Database():

    URI = os.getenv("MONGODB_STRING", "mongodb://mongodb:27017/")

    def __init__(self):
        client = pymongo.MongoClient(self.URI)

        self.DATABASE = client['vagas']

    def insert(self, collection, data):
        return self.DATABASE[collection].insert(data)

    def find_one(self, collection, query):
        return self.DATABASE[collection].find_one(query)

    def find(self, collection, query, sort={"field": "_id", "order": -1}):
        return self.DATABASE[collection].find(query).sort(sort['field'],
                                                          sort['order'])

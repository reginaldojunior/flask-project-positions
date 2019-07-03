import pymongo


class Database():

    URI = "mongodb://127.0.0.1:27017"

    def __init__(self):

        client = pymongo.MongoClient(self.URI)

        self.DATABASE = client['vagas']

    def insert(self, collection, data):
        self.DATABASE[collection].insert(data)

    def find_one(self, collection, query):
        return self.DATABASE[collection].find_one(query)

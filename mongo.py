import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = 'mytestdb'
COLLECTION_NAME = 'myFirstMBD'

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find({'last': 'adams'})

# iterate through the returned mongo object
for doc in documents:
    print(doc)
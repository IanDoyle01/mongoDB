import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = 'mytestdb'
COLLECTION_NAME = 'myFirstMBD'

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

def show_menu():
    print(" ")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")
    
    option = input("Enter option number:")
    return option
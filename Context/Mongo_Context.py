# from pymongo import MongoClient, errors
# from bson.objectid import ObjectId
# from bson import errors as berrors

def connectar():
    conn = MongoClient('localhost', 27017)
    return conn

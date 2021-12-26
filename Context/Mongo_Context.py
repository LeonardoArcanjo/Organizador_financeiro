from pymongo import MongoClient, errors
from bson.objectid import ObjectId
from bson import errors as berrors

def connectar():
    conn = MongoClient('localhost', 27017)
    return conn

def desconnect(conn):
    if conn:
        conn.close()

def insert(name: str, value: float, category: str, instalment: str) -> None: 
    conn = connectar()
    db = conn.pmongo

    try:
        db.financial.insert_one(
            {
                "name": name,
                "value": value,
                "category": category,
                "numberInstalment": instalment
            }
        )
        print(f"{name} was insert successfully!")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")
    
    desconnect(conn)


def list() -> None:

    conn = connectar()
    db = conn.pmongo

    try:
        if db.financial.count_documents({}) > 0:
            documents = db.financial.find()

            print("Listing documents: \n\n")

            for document in documents:
                print(f"name: {document['name']} \
                    value: {document['value']} \
                    category: {document['category']} \
                    Number Instalments: {document['numberInstalment']}")
        else:
            print("There are not elements in DB!")
    except errors.PyMongoError as e:
        print(f"An error occurred: {e}")

    desconnect(conn)


from pymongo import MongoClient

_db=None
_coll=None
def set_db(db):
    global _db
    _db=db
def get_db():
    global _db
    return _db

def set_collection(coll):
    global _coll
    _coll=coll
def get_collection():
    global _coll
    return _coll

def construct_mongo_connection(host, port, username, password, db):
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)
    return conn[db]

def insert_record(db,collection,record):
    return db[collection].insert_one(record)

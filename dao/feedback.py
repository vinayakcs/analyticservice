__author__ = 'crusaderwolf'
from datetime import datetime
from dao import mongo_dao
def get_dateobj():
    utc_time= datetime.utcnow()
    return {
        "y":int(utc_time.strftime("%Y")),
        "m":int(utc_time.strftime("%M")),
        "d":int(utc_time.strftime("%d")),
        "s":int(utc_time.strftime("%s"))
    }

def record_feedback(payload,request_header,ver):
    rec={
        "pld":payload,
        "tst":get_dateobj(),
        "reqhdr":request_header,
        "ver":ver
    }
    mongo_dao.insert_record(mongo_dao.get_db(),
                            mongo_dao.get_collection(),
                            rec)
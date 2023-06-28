from flask import Flask, jsonify, request
import traceback
import json
import os
from dao import mongo_dao,feedback


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
HEADER_EXCLUSION_LIST=['Accept-Encoding',
                       'Accept-Language',
                       'Accept',
                       'Connection',
                       'Cache-Control'
                       ]
def init():
    env=os.environ
    db=mongo_dao.construct_mongo_connection(env.get('host') or 'localhost',
                                         int(env.get('port')) or 27017,
                                         env.get('username') or '',
                                         env.get('password') or '',
                                         env.get('db') or 'feedback')
    mongo_dao.set_db(db)
    mongo_dao.set_collection(env.get('collection') or 'feedback')
    print("Mongo db associated")
    print(mongo_dao.get_db())


try:
    print("Analytics service booting...")
    init()
    print("Initialization complete, ready for service")
except Exception as e:
    print(e)


@app.route("/feedback/v1", methods=['GET','POST'])
def get_insights():
    try:
        requestData=json.loads(request.data.decode('utf-8'))
        reqhdr={}
        for k,v in request.headers:
            if k not in HEADER_EXCLUSION_LIST:
                reqhdr[k]=v
        feedback.record_feedback(requestData,reqhdr,"v1")
        return jsonify({"status": True})
    except Exception as e:
        print(e)
        return jsonify({"status": traceback.format_exc()})

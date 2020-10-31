import os
from flask import Flask, jsonify
application =Flask(__name__)


@application.route('/')
def welcome():
    return jsonify({'status':'application fonctionne'})


if __name__ =='__main__':
    application.run(host="0.0.0.0",port=os.getenv('PORT'))
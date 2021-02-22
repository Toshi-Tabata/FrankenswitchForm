import createDB
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import logging

# TODO: create the flask server to communicate with frontend
# figure out what end points i want
APP = Flask(__name__)
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
cors = CORS(APP)
APP.config['CORS_HEADERS'] = 'Content-Type'


@APP.route("/switches", methods=["GET"])
def switches():
    req = request.data.decode("utf-8")
    print(request.data)
    print(req)
    return jsonify(createDB.get_switches())


@APP.route("/submit", methods=["POST"])
def submit():
    req = request.json
    print(req)
    top = req["top"]["part"][0]
    stem = req["stem"]["part"][0]
    bottom = req["bottom"]["part"][0]
    error = createDB.submitCombo(top, stem, bottom)
    return jsonify({"error": error})


APP.run(port=1337)

createDB.close()

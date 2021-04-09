import accessDB
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from db_helper import get_cursor
import logging

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
    return jsonify(accessDB.get_switches(get_cursor()))


@APP.route("/submit", methods=["POST"])
def submit():
    req = request.json
    print(req)
    if not req:
        return jsonify({"error": "Invalid request given."})
    try:
        top = req["top"]["part"][0]
        stem = req["stem"]["part"][0]
        bottom = req["bottom"]["part"][0]
        info = req["info"]
    except (IndexError, KeyError):
        return jsonify({"error": "Missing valid switch parts"})
    # TODO: pass in the whole object instead
    error = accessDB.submitCombo(top, stem, bottom, get_cursor(), info)
    return jsonify({"error": error})


APP.run(port=1337)

# TODO: Connection never gets closed
# accessDB.close()

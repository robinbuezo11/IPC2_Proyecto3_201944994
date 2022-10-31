from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Pruebas
msg = 'Esta es una prueba'

@app.route('/', methods=["GET"])
def getData():
    return jsonify(msg)

@app.route('/add', methods=["POST"])
def addData():
    body = request.get_json()

    msg += body['msg']

    return jsonify({'msg':'Se agregó la info'})


#Proyecto
@app.route("/fileupload", methods=["GET"])
def getFile():
    return jsonify()
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Pruebas
data = ['Esta es una prueba']

@app.route('/', methods=["GET"])
def getData():
    return jsonify(data)

@app.route('/add', methods=["POST"])
def addData():
    body = request.get_json()

    data.append(body['text'])

    return jsonify({'msg':'Se agregó la info'})

#Proyecto
@app.route("/uploadXml", methods=["POST"])
def uploadXml():
    file = request.get_data().decode()
    file = file[file.find('<'):file.rfind('>')+1]
    print(file)

    return jsonify({'msg': 'Archivo xml cargado exitosamente'})
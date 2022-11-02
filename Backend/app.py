from flask import Flask, jsonify, request
from flask_cors import CORS
from ManagerXml import ManagerXml
from BD import BD

app = Flask(__name__)
CORS(app)

bd = BD('Backend\BD\BD.xml')

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


#--------------------------------Proyecto--------------------------------------

@app.route("/uploadConfigXml", methods=["POST"])
def uploadConfigXml():
    data = request.files['xml']
    #data = data[data.find('<'):data.rfind('>')+1]
    #data = data.replace('\r\n','')
    result = bd.addConfigs(data)

    return jsonify({'msg': result[1]})

@app.route("/uploadConsumedXml", methods=["POST"])
def uploadConsumedXml():
    data = request.files['xml']
    result = bd.addConsumeds(data)

    return jsonify({'msg': result[1]})
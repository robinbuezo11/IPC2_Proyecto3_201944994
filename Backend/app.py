import json
import xmltodict
from flask import Flask, jsonify, request
from flask_cors import CORS
from ManagerXml import ManagerXml
from BD import BD
from Resource import Resource
from Category import Category
from Config import Config
from Client import Client
from Instance import Instance

app = Flask(__name__)
CORS(app)

bd = BD('BD\BD.xml')

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

@app.route("/consultData", methods=["GET"])
def consultData():
    with open('BD\BD.xml','r') as database:
        database = database.read()
        data = xmltodict.parse(database)
        jsondata = json.dumps(data)
        res = json.loads(jsondata)
    return jsonify(res)

@app.route("/createResource", methods=["POST"])
def createResource():
    body = request.get_json()

    id = body['id']
    name = body['name']
    abbrev = body['abbrev']
    metrics = body['metrics']
    type = body['type']
    cost = body['cost']
    
    result = bd.addResource(Resource(id,name,abbrev,metrics,type,cost))

    if result is not None:
        return jsonify({'msg': result})
    else:
        return jsonify({'msg': 'Error al agregar el recurso'})

@app.route("/createCategory", methods=["POST"])
def createCategory():
    body = request.get_json()

    id = body['id']
    name = body['name']
    desc = body['desc']
    workload = body['workload']
    
    result = bd.addCategory(Category(id,name,desc,workload))

    if result is not None:
        return jsonify({'msg': result})
    else:
        return jsonify({'msg': 'Error al agregar la categoria'})

@app.route("/createConfig", methods=["POST"])
def createConfig():
    body = request.get_json()

    idcat = body['idcat']
    id = body['id']
    name = body['name']
    desc = body['desc']
    
    result = bd.addConfig(idcat, Config(id,name,desc))

    return jsonify({'msg': result})

@app.route("/createClient", methods=["POST"])
def createClient():
    body = request.get_json()

    nit = body['nit']
    name = body['name']
    user = body['user']
    passw = body['passw']
    address = body['address']
    email = body['email']
    
    result = bd.addClient(Client(nit,name,user,passw,address,email))

    if result is not None:
        return jsonify({'msg': result})
    else:
        return jsonify({'msg': 'Error al agregar al cliente'})

@app.route("/createInstance", methods=["POST"])
def createInstance():
    body = request.get_json()

    nitclient = body['nitclient']
    idinstance = body['idinstance']
    idconfig = body['idconfig']
    name = body['name']
    startdate = body['startdate']
    status = body['status']
    enddate = body['enddate']
    
    result = bd.addInstance(nitclient, Instance(idinstance,idconfig,name,startdate,status,enddate))

    return jsonify({'msg': result})
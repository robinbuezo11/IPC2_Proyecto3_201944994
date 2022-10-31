import json
import requests

class Services:

    #Pruebas
    def getData():
        return json.loads(requests.get('http://127.0.0.1:5000').text)
        
    def addData(msg):
        response = requests.post('http://127.0.0.1:5000/add', json=msg)
        return json.loads(response.text)
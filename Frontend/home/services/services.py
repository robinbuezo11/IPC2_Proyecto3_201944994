import json
import requests

class Services:

    def uploadConfigXml(xml):
        xml_dict = {'xml': xml}
        response = requests.post('http://127.0.0.1:5000/uploadConfigXml', files=xml_dict)
        return json.loads(response.text)

    def uploadConsumedXml(xml):
        xml_dict = {'xml': xml}
        response = requests.post('http://127.0.0.1:5000/uploadConsumedXml', files=xml_dict)
        return json.loads(response.text)

    def consultData():
        return json.loads(requests.get('http://127.0.0.1:5000/consultData').text)
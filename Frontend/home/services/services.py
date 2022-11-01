import json
import requests

class Services:

    def uploadXml(xml):
        xml_dict = {'xml': xml}
        response = requests.post('http://127.0.0.1:5000/uploadXml', files=xml_dict)
        return json.loads(response.text)
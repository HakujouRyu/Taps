import requests
import base64

class Brewery:
    def __init__(self, json):
        self.json = json

        for k, v in self.json.items():
            setattr(self, k.replace('brewery_',''), v)
        
    def encodeLabel(self):
        self.label_img = base64.b64encode(requests.get(self.label).content)

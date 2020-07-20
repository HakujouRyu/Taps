import requests
import base64
from app.wrappers.Brewery import Brewery

#TODO Make a class for beers


import base64

class Beer:
    def __init__(self, response):
        #TODO Build object by unpacking json response from api
        self.json = response.json()['response']['beer']
        for k, v in self.json.items():
            setattr(self, k.replace('beer_',''), v)


    def encodeLabel(self):
        self.label_img = base64.b64encode(requests.get(self.label).content)

    def getBrewery(self):
        self.brewery = Brewery(self.brewery)
        
    def __str__(self):
        return 'beer'
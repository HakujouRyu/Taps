from decouple import config
from app.wrappers.untappdAPI import API


CLIENTID = config('UNTAPPED_CLIENT_ID')
CLIENTSECRET = config('UNTAPPED_CLIENT_SECRET')

app = API(CLIENTID, CLIENTSECRET)
beer = app.beerInfo('3839')

beer.getBrewery()
beer.encodeLabel()
print(beer.brewery.name)


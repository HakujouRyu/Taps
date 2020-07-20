import requests
from app.wrappers.beer import Beer

class API:
    """An API wrapper object for the V4 Untappd api that requires a {CLIENT_ID} AND A {CLIENT_SECRET}.
    Both are provided by the Untappd dev api.
    """
    def __init__(self, CLIENTID, CLIENTSECRET):
        """Build API wrapper with {CLIENTID} and {CLIENTSECRET}

        Args:
            CLIENTID (int): Developer's Untappd app's client_id
            CLIENTSECRET (int): Developer's Untappd app's client_secret
        """
        self.auth= f'?client_id={CLIENTID}&client_secret={CLIENTSECRET}'
        self.base_url = 'https://api.untappd.com/v4/'
    
    def _get(self, method, query=''):
        """Internal function that returns a {response}

        Args:
            method (str): api call to make
            query (str): search parameters (sometimes optional)

        Returns:
            [type]: [description]
        """
        response = requests.get(self.base_url + method + query + self.auth)
        if response.status_code == 200:
            return response


    def beerInfo(self, beer_id):
        """Returns a {Beer} object with a matching {beer_id}

        Args:
            beer_id (int): The beer's Untappd bid

        Returns:
            Beer: A beer object with many attributes
        """
        method = 'beer/info/'
        response = self._get(method, beer_id)
        beer = Beer(response)
        return beer

    def beerSearch(self, query):
        pass


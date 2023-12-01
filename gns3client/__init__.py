__author__ = 'Jason Hall'
__email__ = 'jdhall75@zohomail.com'
__version__ = '0.1.0'

import requests
from gns3client.endpoints.compute import Compute
from gns3client.endpoints.appliance import Appliance

class InvalidParameters(Exception):
    """ Raised when response status code is 400 """
    pass

class NotFound(Exception):
    """ Raised when API response has status code 404 """
    pass

class HttpError(Exception):
    """ Generic HTTP exception for all other HTTP error code"""
    pass


class Api():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.base_url = ""
        self.session = requests.Session()

    def _make_request(self, url:str, method:str="GET", params:dict={}, headers={}):
        url = self.base_url + url
        resp = self.session.request(method, url, params=params, headers=headers)

        if resp.status_code == 400:
            raise InvalidParameters(f"{url} returned 400")
        elif resp.status_code == 404:
            raise NotFound(f"{url} return 404 the resource cant be found")
        elif resp.status_code >= 400 <= 500:
            raise HttpError(f"calling {method} {url} with params {params} resulted in a {resp.status_code}")

        return resp

    def _authenticate(self):
        pass

api = Api()

api.compute = Compute(api)
api.appliance = Appliance(api)


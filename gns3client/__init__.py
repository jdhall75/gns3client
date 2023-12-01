__author__ = 'Jason Hall'
__email__ = 'jdhall75@zohomail.com'
__version__ = '0.1.0'

import requests
from gns3client.endpoints.compute import Compute
from gns3client.endpoints.appliance import Appliance

class Api():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.base_url = ""
        self.session = requests.Session()

    def _make_request(self, url:str, method:str="GET", params:dict={}, headers={}):
        url = self.base_url + url
        resp = self.session.request(method, url, params=params, headers=headers)
        return resp

    def _authenticate(self):
        pass

api = Api()

api.compute = Compute(api)
api.appliance = Appliance(api)


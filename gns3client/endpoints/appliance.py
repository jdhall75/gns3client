
class Appliance():
    def __init__(self, api_ref):
        self.api_ref = api_ref

    def get_appliances(self):
        """ get appliances that have been configured on the gns3 server """
        url = "/v2/appliances"
        return self.api_ref._make_request(method="GET", url=url)

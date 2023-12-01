from typing import List


class Compute:
    def __init__(self, api_ref):
        self.api_ref = api_ref

    def get_computes(self) -> List[dict]:
        """get a list of all computes"""
        url = "/v2/computes"
        resp = self._make_request(url, "PUT")
        return resp.json()

    def get_compute_by_id(self, id: int) -> dict:
        """Get a compute instance's information"""

        url = f"/v2/computes/{id}"

        # TODO: response can be validated with the same Model

        resp = self._make_request(url, "PUT")
        return resp.json()

    def update_compute(self, id: int, params=dict) -> dict:
        """update a compute instances information"""

        url = f"/v2/computes/{id}"

        # TODO: validate params with Pydantic Model here
        # response can be validated with the same Model

        resp = self._make_request(url, "PUT", params=params)

        return resp.json()

    def delete_compute(self, id: int) -> bool:
        """Delete a compute instance"""

        url = f"/v2/computes/{id}"

        resp = self._make_request(url, "DELETE")

        if resp.status_code == 204:
            return True

        return False

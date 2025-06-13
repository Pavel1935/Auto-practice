import requests
from constants import Constants

class TestDeleteVerifyLogin():

    def test_delete_verify_login(self):
        response = requests.delete(Constants.DELETE_to_verify_login)

        assert response.status_code == 200
        assert response.json() == {"responseCode": 405, "message": "This request method is not supported."}
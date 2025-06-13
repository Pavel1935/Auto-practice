import requests
from constants import Constants

class TestVerifyLoginWithInvalidDetails():

    @classmethod
    def setup_class(cls):
        cls.user_data = {
            'email': 'oukb11147@gmail.com',
            'password': 'Qwerty1123!'
        }

    def test_verify_login_with_invalid_details(self):
        payload = self.user_data
        response = requests.post(Constants.POST_to_verify_login_with_invalid_details, data=payload)
        assert response.status_code == 200
        assert response.json() == {"responseCode": 404, "message": "User not found!"}

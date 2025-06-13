import requests
from constants import Constants

class TestToVerifyLoginWithoutEmail():
    @classmethod
    def setup_class(cls):
        cls.user_data = {
            'password': 'Qwerty123!'
        }
    def test_to_verify_login_without_email_parameter(self):
        payload = self.user_data
        response = requests.post(Constants.POST_to_verify_login_without_email_parameter, data=payload)

        assert response.status_code == 200
        assert (response.json() ==
                {"responseCode": 400, "message": "Bad request, email or password parameter is missing in POST request."})

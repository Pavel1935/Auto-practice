import requests
from constants import Constants

class TestToVerifyLoginWithValidDetails():
    @classmethod
    def setup_class(cls):
        cls.user_data = {
            'email': 'oukb1147@gmail.com',
            'password': 'Qwerty123!'
        }
    def test_to_verify_login_with_valid_details(self):
        payload = self.user_data
        response = requests.post(Constants.POST_To_Verify_Login_with_valid_details_URL, data=payload)

        assert response.status_code == 200
        assert response.json() == {"responseCode": 200, "message": "User exists!"}

import requests
from constants import Constants

class TestDeleteMethodToDeleteUserAccount():
    @classmethod
    def setup_class(cls):
        cls.user_data = {
            'email': 'oukb1147@gmail.com',
            'password': 'Qwerty123!'
        }

    def test_delete_method_to_delete_user_account(self):
        payload = self.user_data
        response = requests.delete(Constants.DELETE_METHOD_To_Delete_User_Account, data=payload)
        assert response.status_code == 200
        assert response.json() == {"responseCode": 200, "message": "Account deleted!"}

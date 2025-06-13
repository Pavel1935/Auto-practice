import requests
from constants import Constants

class TestUserAccountDetailByEmail():
    
    params = {
        "email": "oukb37@gmail.com"  # замените на нужный email
    }
    def test_user_account_detail_by_email(self):
        response = requests.get(Constants.GET_user_account_detail_by_email, params=self.params)
        assert response.status_code == 200
        json_data = response.json()

        assert json_data["responseCode"] == 200
        assert "user" in json_data
        assert json_data["user"]["email"] == self.params["email"]

import requests
from constants import Constants

class TestCreateRegisterUserAccount():

        @classmethod
        def setup_class(cls):
            cls.user_data = {
                'name': 'skin',
                'email': 'oukb2347@gmail.com',
                'password': 'Qwerty1123!',
                'title' : 'Mr',
                'birth_date': '30',
                'birth_month': '7',
                'birth_year': '1',
                'firstname': 'Mih',
                'lastname': 'Him!',
                'company': 'FCSM',
                'address1': 'Jkjwbef',
                'address2': 'Jkjwbef',
                'country': 'india',
                'zipcode': '123456',
                'state': 'Minisota',
                'city': 'Minisota',
                'mobile_number': '+79999999999'
            }
        def test_create_register_user_account(self):
            payload = self.user_data
            response = requests.post(Constants.POST_To_Create_Register_User_Account, data=payload)
            assert response.status_code == 200
            assert response.json() == {"responseCode": 201, "message": "User created!"}
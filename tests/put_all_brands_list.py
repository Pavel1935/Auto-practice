import requests
from faker import Faker
faker = Faker()
from constants import Constants

class TestPutAllBrandsList():

    def test_put_to_all_brands_list(self):
        response = requests.put(Constants.PUT_To_All_Brands_List_URL)
        assert response.status_code == 200 and response.json() == {
        "responseCode": 405,
        "message": "This request method is not supported."
    }


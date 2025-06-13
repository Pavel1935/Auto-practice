import requests
from faker import Faker
faker = Faker()
from constants import Constants

class TestAllBrandsList():

    def test_get_all_brands_list(self):
        response = requests.get(Constants.Get_All_Brands_List_URL)
        assert response.status_code == 200


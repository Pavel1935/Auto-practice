import allure
import requests
from faker import Faker
faker = Faker()
from constants import Constants

class TestGetProductsList():

    def test_get_products_list(self):
        response = requests.get(Constants.Get_All_Products_List_URL)
        assert response.status_code == 200


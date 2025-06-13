import allure
import requests
from faker import Faker
faker = Faker()
from constants import Constants

class TestToAllProductsList():

    def test_post_to_all_products_list(self):
        response = requests.post(Constants.POST_To_All_Products_List_URL)
        assert response.status_code == 200

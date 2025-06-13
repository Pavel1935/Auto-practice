import requests
from constants import Constants

class TestToSearchProduct():
    def test_to_search_product(self):
        payload = {
            "search_product": "top"  # или "tshirt", "jean", и т.д.
        }
        response = requests.post(Constants.POST_To_Search_Product_URL, data=payload)
        assert response.status_code == 200

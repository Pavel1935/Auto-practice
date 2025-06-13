import requests
from constants import Constants

class TestToSearchProductWithout():
    def test_to_search_product(self):
        response = requests.post(Constants.POST_To_Search_Product_without_URL)
        assert (response.status_code == 200 and response.json() ==
                {"responseCode": 400, "message": "Bad request, search_product parameter is missing in POST request."})

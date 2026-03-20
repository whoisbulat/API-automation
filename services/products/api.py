import allure
import requests
from utils.helper import Helper
from config.headers import Headers
from services.products.payloads import Payloads
from services.products.endpoints import Endpoints
from services.products.models.model_products import ProductResponse



class UsersAPI(Helper):

    def __init__(self):
        self.payloads = Payloads()
        self.headers = Headers()
        self.endpoints = Endpoints()

    @allure.step("Get products list")
    def get_products_list(self) -> ProductResponse:
        response = requests.get(
            url=self.endpoints.products_list,
            headers=self.headers.basic,
            verify= False
        )
        return self.validate_response(response, ProductResponse)
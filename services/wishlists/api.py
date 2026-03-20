import allure
import requests
# import requests_ai_validator as requests
from utils.helper import Helper
from config.headers import Headers
from services.wishlists.payloads import Payloads
from services.wishlists.endpoints import Endpoints
from services.wishlists.models.model_wishlist import ItemsResponse


class WishlistsAPI(Helper):

    def __init__(self):
        self.payloads = Payloads()
        self.headers = Headers()
        self.endpoints = Endpoints()

    @allure.step("Get wishlist by uuid")
    def get_wishlist_by_uuid(self, uuid) -> list[ItemsResponse]:
        response = requests.get(
            url=self.endpoints.get_wishlist_by_uuid(uuid),
            headers=self.headers.basic,
            verify= False
        )
        self.validate_response(response, ItemsResponse)



import allure
from config.base_test import BaseTest

@allure.epic("Products")
@allure.feature("Product Catalog")
class TestUsers(BaseTest):

    @allure.title("Get products list")
    def test_create_user(self):
       self.users_api.get_products_list()

конфликт


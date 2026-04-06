import allure
import pytest

from config.base_test import BaseTest

@allure.epic("Products")
@allure.feature("Product Catalog")
class TestUsers(BaseTest):

    @pytest.mark.smoke
    @allure.title("Get products list")
    def test_create_user(self):
       self.users_api.get_products_list()


    @allure.title("Get products list_!")
    def test_create_user_2(self):
       self.users_api.get_products_list()






import pytest

from services.products.api import UsersAPI
from services.wishlists.api import WishlistsAPI


class BaseTest:

    def setup_method(self):
        self.users_api = UsersAPI()
        self.wishlists_api = WishlistsAPI()


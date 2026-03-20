from config.stages import get_stage

STAGE = get_stage()

class Endpoints:

    def get_wishlist_by_uuid(self, uuid):
        return f"{STAGE}/users/{uuid}/wishlist"
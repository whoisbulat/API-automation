from config.stages import get_stage

STAGE = get_stage()

class Endpoints:

    products_list = f"{STAGE}/products"

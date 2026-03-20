import os
from dotenv import load_dotenv

load_dotenv()
#
# def get_token():
#     token = "213"
#     os.environ["API_TOKEN"] = token
#
# get_token()

class Headers:


    # def basic(self, x_task_id: str):
    #     return {
    #         "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
    #         "X-Task-Id": x_task_id
    #     }

    basic = {
        "Authorization": f"Bearer {os.getenv('API_TOKEN')}",
        "X-Task-Id": "api-3"
    }


print(Headers.basic)
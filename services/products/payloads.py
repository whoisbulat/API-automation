from faker import Faker

faker = Faker()

class Payloads:

    def create_user(self, email: str = faker.email(), nickname: str = faker.user_name()):
        return {
          "email": email,
          "password": faker.password(),
          "name": faker.name(),
          "nickname": nickname
        }



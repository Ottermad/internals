from faker import Faker


fake = Faker()


class UserFactory:
    def new(self):
        user = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'username': fake.user_name(),
            'password': fake.password(),
            'pk': fake.random_int()
        }

        return user

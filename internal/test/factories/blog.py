from faker import Faker
import random

fake = Faker()


class BlogFactory:
    def new(self, user=None):
        text = fake.text()
        blogpost = {
            'pk': fake.random_int(),
            'title': fake.first_name(),
            'markdown': text,
            'html': text,
            'published': bool(random.randint(0, 1)),
            'published_at': fake.date_time_this_month(before_now=True)
        }

        if user is not None:
            blogpost['author_id'] = user['id']
        else:
            blogpost['author_id'] = fake.random_int()

        return blogpost

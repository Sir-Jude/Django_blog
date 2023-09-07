from blog.models import Game
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from faker import Faker
from faker_food import FoodProvider

fake = Faker()
fake.add_provider(FoodProvider)


def run():
    Food.objects.all().delete()
    print("Flushed out data... recreating!")
    try:
        u = User.objects.get(username="fake_admin")
    except Exception as e:
        u = User.objects.create(
            username="fake_admin", password="password1234", email="test@example.com"
        )

    NUMBER = 10
    for _ in range(NUMBER):
        f = Food.objects.create(
            name=fake.dish(),
            origin=fake.ethnic_category(),
            recipe=fake.ingredient(),
            date_of_expiry=datetime.now() + timedelta(days=366),
        )
        print(f"{f} created!")
    print()
    print(f"{NUMBER} foods have been created, please note they are fake!")

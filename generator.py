import random
from data import Person
from faker import Faker

fake = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=fake.first_name() + " " + fake.last_name() + " " + fake.middle_name(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        age=random.randint(15, 100),
        salary=random.randint(100, 5000),
        department=fake.job(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address()
    )

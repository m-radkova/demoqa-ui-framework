from data import Person
from faker import Faker

fake = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=fake.first_name() + " " + fake.last_name() + " " + fake.middle_name(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address()
    )
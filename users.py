from faker import Faker
from faker.providers import profile

if __name__ == "__main__":
    fake = Faker()
    fake.add_provider(profile)

    print(fake.profile())

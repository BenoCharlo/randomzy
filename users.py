import csv
import datetime
import random
from pathlib import Path
import boto3
from faker import Faker
from faker.providers import profile

import settings

N_PROFILES = random.randint(settings.MIN_PROFILES, settings.MAX_PROFILES)
FILENAME = str(datetime.datetime.now()).replace(" ", "_") + ".csv"


fake = Faker()
fake.add_provider(profile)


def generate_profiles() -> list:
    return [fake.profile() for _ in range(N_PROFILES)]


# create temp folder
Path("temp").mkdir(exist_ok=True)


def save_profiles(profiles: list, filepath: Path) -> str:

    with open(filepath, "w") as file:
        csv_w = csv.writer(file, delimiter="|")
        csv_w.writerows(profiles)

    return "=" * 5, "File saving done", "=" * 5


if __name__ == "__main__":
    save_profiles(profiles=generate_profiles(), filepath=Path("temp", FILENAME))

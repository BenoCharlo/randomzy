import datetime
import random
from pathlib import Path

import boto3
import pandas as pd
from faker import Faker
from faker.providers import profile

import settings
import helpers

N_PROFILES = random.randint(settings.MIN_PROFILES, settings.MAX_PROFILES)
FILENAME = str(datetime.datetime.now()).replace(" ", "_") + ".csv"


fake = Faker()
fake.add_provider(profile)


def generate_profiles() -> list:
    return [fake.profile() for _ in range(N_PROFILES)]


helpers.create_folder()


def save_profiles(profiles: list, filepath: Path) -> str:
    return pd.DataFrame(profiles).to_csv(filepath, sep="|", index=False)


if __name__ == "__main__":
    save_profiles(profiles=generate_profiles(), filepath=Path("temp", FILENAME))
    helpers.delete_folder()

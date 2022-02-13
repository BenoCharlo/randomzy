import datetime
import random
from pathlib import Path

import pandas as pd
from faker import Faker
from faker.providers import profile

import settings as settings

N_PROFILES = random.randint(settings.MIN_PROFILES, settings.MAX_PROFILES)
FILENAME = str(datetime.datetime.now()).replace(" ", "_") + ".csv"


fake = Faker()
fake.add_provider(profile)


def generate_profiles() -> list:
    return [fake.profile() for _ in range(N_PROFILES)]


def save_profiles(profiles: list, filepath: Path) -> str:
    return pd.DataFrame(profiles).to_csv(filepath, sep="|", index=False)

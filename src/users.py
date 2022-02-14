from pathlib import Path

import pandas as pd
from faker import Faker
from faker.providers import profile


fake = Faker()
fake.add_provider(profile)


def generate_profiles(n_profiles: int) -> list:
    return [fake.profile() for _ in range(n_profiles)]


def save_profiles(profiles: list, filepath: Path) -> str:
    return pd.DataFrame(profiles).to_csv(filepath, sep="|", index=False)

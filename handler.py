import os
import datetime
import random

from pathlib import Path
import boto3

from src import helpers, users, settings


N_PROFILES = random.randint(settings.MIN_PROFILES, settings.MAX_PROFILES)
FILENAME = str(datetime.datetime.now()).replace(" ", "_") + ".csv"


def main(event, context):
    helpers.create_folder()
    users.save_profiles(
        profiles=users.generate_profiles(N_PROFILES), filepath=Path(settings.TEMP_FOLDER, FILENAME)
    )
    access_key = os.getenv("ACCESS_KEY")
    secret_key = os.getenv("SECRET_KEY")
    bucket_name = os.getenv("BUCKET")

    s3 = boto3.client("s3", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    s3.upload_file(str(Path(settings.TEMP_FOLDER, FILENAME)), bucket_name, FILENAME)

    helpers.delete_folder()


if __name__ == "__main__":
    main("", "")

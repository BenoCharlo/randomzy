# randomzy
[![Python 3.7.4](http://img.shields.io/badge/python-3.7.4-blue.svg)](https://www.python.org/downloads/release/python-379/)

Randomzy is an data pipeline based on AWS infrastucture for data ingestion. A set of random data is generated by python library _Faker_. The data is then It uses lambda function to perform ingestion of the  data to an S3 bucket. Another lambda function is then triggered to insert the data in a postgres dataset. And finally, we ran a simple _great-expectations_ function to validate the data based on some conditions.

The following picture shows the complete schema of the architecture.


&copy; *Beno-Charles DOKODJO, Technology | Serverless | Cloud*
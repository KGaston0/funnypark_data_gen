import os
from datetime import datetime, timedelta
import random
from faker import Faker

faker = Faker("es_AR")

def random_date(start_year=2020, end_year=2025):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))

def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

def clean_name(name):
    return name.strip().lower().replace('"', '').replace('`', '').replace("'", "")

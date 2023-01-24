import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Core.settings')

from random import randrange

import django 
django.setup()

from faker import Faker
from django.contrib.auth.models import User



def set_user():
    fake = Faker(['az_AZ']) 
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f"{f_name.lower()}_{l_name.lower()}"
    email = f"{u_name}@{fake.domain_name()}"
    user_check = User.objects.filter(username=u_name,email=email)
    if user_check.exists():
        set_user()
    user = User(
        username = u_name,
        email=email
    )
    user.set_password("parol_x")
    user.save()



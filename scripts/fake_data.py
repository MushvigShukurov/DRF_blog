import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Core.settings')

from random import randrange

import django 
django.setup()

from faker import Faker
from django.contrib.auth.models import User
from blog.api.serializers import UserSerializer


def set_user():
    fake = Faker(['az_AZ']) 
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f"{f_name.lower()}_{l_name.lower()}"
    user_check = User.objects.filter(username=u_name)
    if user_check.exists():
        u_name += randrange(1000,10000)
    user = User(
        username = u_name
    )
    user.set_password("qwerty123")
    user = {
        "username":user.username,
        "password":user.password
    }
    serializer = UserSerializer(data=user)
    if serializer.is_valid():
        serializer.save()


def users_count():
    return User.objects.all().count()
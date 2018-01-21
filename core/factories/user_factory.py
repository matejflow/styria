import random

import factory

from django.contrib.auth.models import User


def superuser_calc(is_staff):
    if not is_staff:
        return False
    else:
        return (random.getrandbits(1))


class UserFactory(factory.django.DjangoModelFactory):
    """
    Base factory for creating user instances
    """
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')
    is_active = factory.Faker('boolean')
    is_staff = factory.Faker('boolean')

    @factory.lazy_attribute
    def is_superuser(self):
        if not self.is_staff:
            return False
        else:
            return (random.getrandbits(1))


class MemberFactory(UserFactory):
    is_staff = False


class StaffFactory(UserFactory):
    is_staff = True
    is_superuser = False


class SuperUserFactory(UserFactory):
    is_staff = True
    is_superuser = True

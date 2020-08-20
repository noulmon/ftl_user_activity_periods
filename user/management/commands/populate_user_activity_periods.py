import random
import string
from datetime import timedelta

import pytz
from django.core.management.base import BaseCommand
from faker import Faker

from user.models import User, UserActivityPeriod

fake = Faker()


def generate_key():
    """
    :return: Random unique key as user id
    """
    letters_and_digits = string.ascii_uppercase + string.digits
    unique_id = 'W0' + ''.join((random.choice(letters_and_digits) for i in range(7)))
    # returns true generated id is unique
    if is_id_unique(unique_id):
        return unique_id
    generate_key()


def is_id_unique(unique_id):
    """ Checks the uniqueness of the user id """
    try:
        User.objects.get(unique_id=unique_id)
    # checks whether the user is unique or not
    except User.DoesNotExist:
        return True
    return False


def generate_random_fake_name():
    """ Generates random fake name for user"""
    return fake.name()


def generate_random_time_zone():
    # generates random timezone for user
    return random.choice(pytz.all_timezones)


class Command(BaseCommand):
    def handle(self, *args, **options):
        activity_period_list = []
        # populating DB with 100 user data and some activity periods
        for _ in range(100):
            # user fullname
            name = generate_random_fake_name().split()
            # timezone
            tz = generate_random_time_zone()
            # creating user
            user = User.objects.create(unique_id=generate_key(), first_name=name[0], last_name=name[1], timezone=tz)
            print(f'created user: {" ".join(name)}')
            # creating activity periods for users(between 3 and 8 for each)
            for _ in range(random.choice(range(3, 8))):
                # start time
                star_time = fake.date_time_this_year()
                # end time
                end_time = star_time + timedelta(hours=random.choice(range(1, 10)))
                activity_period_list.append(UserActivityPeriod(user=user, start_time=star_time, end_time=end_time))
                print('created random activity period for user')
        # creating user activity period against user name
        UserActivityPeriod.objects.bulk_create(activity_period_list)
        print('Data population completed!')

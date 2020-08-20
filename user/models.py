import pytz
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    unique_id = models.CharField(_('First ID'), max_length=100, unique=True, blank=True, default='')
    first_name = models.CharField(_('First name'), max_length=30, blank=True, default='')
    last_name = models.CharField(_('Last name'), max_length=30, blank=True, default='')
    timezone = models.CharField(_('Timezone'), max_length=100, choices=TIMEZONES, default='UTC')

    USERNAME_FIELD = 'unique_id'

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return '%s %s' % (self.first_name, self.last_name)


class UserActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return "{}({} - {})".format(self.user.unique_id, self.start_time, self.end_time)

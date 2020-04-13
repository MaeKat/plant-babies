from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from dateutil.relativedelta import relativedelta

class CustomUser(AbstractUser):
    # These are the fields we want on top of the fields included
    #  with the built-in Django User Model that come with:
    #  username, first_name, last_name, email, password, ....
    gender = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    def age(self):
        if self.dob == None:
            return None
        age = relativedelta(date.today(), self.dob)
        return age.years

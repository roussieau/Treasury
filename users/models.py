from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    treasurer = models.BooleanField(default = False)

    def __str__(self):
        return self.email
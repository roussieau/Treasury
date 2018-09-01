from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Kot(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return '{} - {}'.format(self.name, self.year)

class CustomUser(AbstractUser):
    # add additional fields in here
    treasurer = models.BooleanField(default = False)
    kot = models.ForeignKey(Kot, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.get_full_name()



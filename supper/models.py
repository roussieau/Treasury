from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Day(models.Model):
    date = models.DateField()
    week = models.IntegerField(default=0)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return 'S{} - {: %d/%m/%y}'.format(self.week, self.date)

    def presence(self, user):
        return Participation.objects.filter(user=user, day=self).exists()

class Participation(models.Model):
    user = models.ForeignKey('users.CustomUser',on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    weight = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return '{} au souper du {: %d/%m}'.format(self.user.get_full_name(), self.day.date)

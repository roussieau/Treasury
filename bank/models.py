from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class Expense(models.Model):
    date = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=60, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0.01)])
    positive = models.BooleanField(default=False)
    added_by = models.ForeignKey('users.CustomUser',on_delete=models.CASCADE, blank=True) 
    kot = models.ForeignKey('users.Kot', on_delete=models.CASCADE)
    day = models.ForeignKey('supper.Day',on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        date_with_timezone = timezone.localtime(self.date)
        return "{}({}) le {:%d/%m/%y à %H:%M} pour {}€".format(self.added_by.get_full_name(),
                self.kot.name, date_with_timezone, self.cost)

    def debit(self, users):
        numberOfUsers = len(users)
        costPerPerson = self.cost / numberOfUsers
        for u in users:
            t = Transaction(cost=costPerPerson, expense=self, user=u)
            t.save()
            
    def date_to_string(self):
        date_with_timezone = timezone.localtime(self.date)
        return '{:%d/%m/%y %H:%M}'.format(date_with_timezone)

class Transaction(models.Model):
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    positive = models.BooleanField(default=False)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        date_with_timezone = timezone.localtime(self.expense.date)
        return "{} le {: %d/%m/%Y à %H:%M}".format(self.user.get_full_name(), date_with_timezone)

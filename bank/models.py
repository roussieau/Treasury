from django.db import models
from users.models import CustomUser, Kot
from django.utils import timezone

# Create your models here.
class Expense(models.Model):
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=300, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    added_by = models.ForeignKey(CustomUser,on_delete=models.CASCADE, blank=True) 
    kot = models.ForeignKey(Kot, on_delete=models.CASCADE)

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
            

class Transaction(models.Model):
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    positive = models.BooleanField(default=False)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        date_with_timezone = timezone.localtime(self.expense.date)
        return "{} le {: %d/%m/%Y à %H:%M}".format(self.user.get_full_name(), date_with_timezone)

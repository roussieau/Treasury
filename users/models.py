from django.db import models
from django.contrib.auth.models import AbstractUser
from bank.models import Transaction, Expense

# Create your models here.
class Kot(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField(default=0)
    balance = models.IntegerField(default=0)
    password = models.CharField(default="password", max_length=30)

    def __str__(self):
        return '{} - {}'.format(self.name, self.year)

    @property
    def balance(self):
        listOfExpenses = Expense.objects.filter(kot=self)
        balance = 0
        for e in listOfExpenses:
            balance += e.cost

        return balance

class CustomUser(AbstractUser):
    # add additional fields in here
    treasurer = models.BooleanField(default = False)
    kot = models.ForeignKey(Kot, on_delete=models.CASCADE, null=True)
    internal = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name()

    @property
    def balance(self):
        listOfTransactions = Transaction.objects.filter(user=self)
        balance = 0
        for t in listOfTransactions:
            if t.positive:
                balance += t.cost
            else:
                balance -= t.cost
        return balance

    def get_transactions(self):
        return Transaction.objects.filter(user=self).order_by('-expense__date')[:30]
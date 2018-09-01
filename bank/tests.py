from django.test import TestCase
from .models import Expense
from users.models import CustomUser, Kot
from .models import Expense, Transaction

# Create your tests here.
class BankModelTestCase(TestCase):
    def setUp(self):
        self.j = CustomUser.objects.create_user(username='Julian')
        t = CustomUser.objects.create_user(username='Thomas')
        c = CustomUser.objects.create_user(username='Charles')
        self.listOfUsers = [self.j, t, c] 
        self.kot = Kot.objects.create(name='Kot de test')

    def test_expense_debit(self):
        e = Expense(cost=15, kot=self.kot, added_by=self.j)
        e.save()
        e.debit(self.listOfUsers)
        
        t = Transaction.objects.get(user=self.j, expense=e )
        self.assertEqual(t.cost, 5)


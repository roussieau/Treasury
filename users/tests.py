from django.test import TestCase
from .models import CustomUser
from bank.models import Transaction

# Create your tests here.
class BalanceTestCase(TestCase):
	def test_user_balance_positive(self):
		user = CustomUser.objects.create(username='julian')
		Transaction.objects.create(cost=5, user=user)
		Transaction.objects.create(cost=10, user=user)
		Transaction.objects.create(cost=18, positive=True, user=user)
		self.assertEqual(user.get_balance(), 3) 

	def test_user_balance_negative(self):
		user = CustomUser.objects.create(username='julian')
		Transaction.objects.create(cost=5, user=user)
		Transaction.objects.create(cost=10, user=user)
		self.assertEqual(user.get_balance(), -15) 
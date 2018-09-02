from django.forms import ModelForm 
from django import forms
from .models import Expense
from users.models import CustomUser

class ExpenseForm(ModelForm):
    users = forms.ModelMultipleChoiceField(CustomUser.objects.all(), label='Utilisateurs')

    paid_with_my_card = forms.BooleanField(label="Payé avec ma carte", required=False)
    class Meta: 
        model = Expense
        fields = ['cost', 'description']
        labels = {
        	"cost": "Montant",
    	}

class AddMoneyForm(ModelForm):
	user = forms.ModelChoiceField(CustomUser.objects.all(), label='Utilisateur')
	class Meta:
		model = Expense
		fields = ['date', 'cost', 'description']
		labels = {
        	"cost": "Montant",
    	}
from django.forms import ModelForm 
from django import forms
from .models import Expense
from users.models import CustomUser

class ExpenseForm(ModelForm):
    users = forms.ModelMultipleChoiceField(CustomUser.objects.all(), label='Utilisateurs')
    
    class Meta: 
        model = Expense
        fields = ['cost', 'description']
        labels = {
        	"cost": "Montant",
    	}

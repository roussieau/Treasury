from django import forms

class DayExpenseForm(forms.Form):
    cost = forms.DecimalField(label='Montant', decimal_places=2, min_value=0)
    description = forms.CharField(label='Description')

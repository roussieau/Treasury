from django import forms

class DayExpenseForm(forms.Form):
    cost = forms.DecimalField(label='Montant', decimal_places=2, min_value=0)
    description = forms.CharField(label='Description')

    def __init__(self, user, *args, **kwargs):
        super(DayExpenseForm, self).__init__(*args, **kwargs)
        if user.kot.tricountOnly:
            self.fields['paid_with_my_card'] = forms.BooleanField(initial=True, widget=forms.HiddenInput())
        else:
            self.fields['paid_with_my_card'] = forms.BooleanField(label="Payé avec ma carte", required=False)

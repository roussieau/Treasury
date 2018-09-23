from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Kot

class CustomUserCreationForm(UserCreationForm):
	firstname = forms.CharField(label="Prénom", max_length=30)
	lastname = forms.CharField(label="Nom", max_length=30)
	mail = forms.EmailField(label="Adresse mail", max_length=100)
	kot = forms.ModelChoiceField(Kot.objects.all())
	kotPassword = forms.CharField(label="Mot de passe du kot", max_length=30)

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = UserCreationForm.Meta.fields 

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'treasurer')

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
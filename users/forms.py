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

	def clean(self):
		cleaned_data = super(CustomUserCreationForm, self).clean()
		kot = cleaned_data['kot']
		password = cleaned_data['kotPassword']

		if kot.password != password:
			self.add_error('kotPassword',
				"Le mot de passe ne correspond à celui de votre kot.")
		return cleaned_data

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'treasurer')

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
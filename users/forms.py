from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Kot
from django.contrib.auth import authenticate

class CustomUserCreationForm(UserCreationForm):
	firstname = forms.CharField(label="Prénom", max_length=30)
	lastname = forms.CharField(label="Nom", max_length=30)
	mail = forms.EmailField(label="Adresse mail", max_length=100)
	internal = forms.BooleanField(label="Interne", required=False)
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

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("La combinaison nom d'utilisateur/mot de passe est invalide")
		return self.cleaned_data
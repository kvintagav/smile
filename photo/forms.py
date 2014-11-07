from django import forms
from photo.models import Photographer
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confimation',widget=forms.PasswordInput)

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1!=password2:
			raise forms.ValidationError("Password don't match")
		return password2

	def save(self, commit = True):
		Photographer = super(UserCreationForm, self).save(commit=False)
		Photographer.set_password(self.cleaned_data["password1"])
		if commit:
			Photographer.save()
		return Photographer


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()



    def clean_password(self):
        return self.initial["password"]
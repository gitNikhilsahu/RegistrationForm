from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=15, label="Username")
    firstname = forms.CharField(max_length=15, label="Firstname")
    lastname = forms.CharField(max_length=15, label="Lastname")
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password1 = forms.CharField(widget=forms.PasswordInput, label="PasswordConfirmation")

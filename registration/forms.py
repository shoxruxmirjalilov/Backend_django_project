from django import forms
from django.core import validators
#DataFlair #Form
class SignUp(forms.Form):
  first_name = forms.CharField(initial = 'First Name', )
  last_name = forms.CharField(required = False)
  email = forms.EmailField(help_text = 'write your email', required = False)
  Address = forms.CharField(required = False, )
  Technology = forms.CharField(initial = 'Django', disabled = True)
  age = forms.IntegerField(required = False, )
  password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
  re_password = forms.CharField(widget = forms.PasswordInput, required = False)
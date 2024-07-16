from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms

class LoginRegisterForm(AuthenticationForm):
    username = forms.CharField(required = True, widget=forms.TextInput(attrs={ 'placeholder': 'Username', 'id': 'usrname', 'minlength': 2, 'required': True}))
    password = forms.CharField(required = True, widget=forms.PasswordInput(attrs={ 'placeholder': 'Password', 'id': 'passwd', 'minlength': 6}))
   # email = forms.CharField(required = True, widget=forms.EmailInput(attrs={ 'placeholder': 'E-mail', 'id': 'e_mail'}))
    rememberme = forms.BooleanField(label = 'Remeber me', required = False, widget=forms.CheckboxInput())
 
    class Meta:
        model = get_user_model()
        fields = ['username', 'password','rememberme']
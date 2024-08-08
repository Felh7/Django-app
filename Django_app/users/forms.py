from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm,PasswordResetForm
from django.contrib.auth import get_user_model
from django import forms

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(required = True, widget=forms.TextInput(attrs={ 'placeholder': 'Username', 'id': 'usrname', 'minlength': 2, 'maxlength': 24}))
    password = forms.CharField(required = True, widget=forms.PasswordInput(attrs={ 'placeholder': 'Password', 'id': 'passwd', 'minlength': 6, 'maxlength': 32}))
   # email = forms.CharField(required = True, widget=forms.EmailInput(attrs={ 'placeholder': 'E-mail', 'id': 'e_mail'}))
    rememberme = forms.BooleanField(label = 'Remeber me', required = False, widget=forms.CheckboxInput())
 
    class Meta:
        model = get_user_model()
        fields = ['username', 'password','rememberme']
    
    error_messages = {
        "invalid_login": (
            "Wrong username or password"
        ),
    }

class RegisterUserForm(UserCreationForm):
    username =  forms.CharField(required = True, widget=forms.TextInput(attrs={ 'placeholder': 'Username', 'id': 'usrname', 'minlength': 2, 'maxlength': 24}))
    password1 = forms.CharField(required = True, widget=forms.PasswordInput(attrs={ 'placeholder': 'Password', 'id': 'passwd', 'maxlength': 32 }))
    password2 = forms.CharField(required = True, widget=forms.PasswordInput(attrs={ 'placeholder': 'Repeat your password', 'id': 'passwdrpt', }))
    email = forms.CharField(required = True, widget=forms.EmailInput(attrs={ 'placeholder': 'E-mail', 'id': 'e_mail'}))

    error_messages = {
        "password_mismatch": ("Passwords didn’t match."),
    }

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email = email).exists():
            raise forms.ValidationError("This e-mail already exists")
        return email

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'placeholder': 'E-mail', 'id': 'e_mail'}),
    )
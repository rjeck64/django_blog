from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label=False, max_length=255, widget=forms.TextInput(attrs={"class": "form-control form-control-user","placeholder" : "Username..."}))
    email = forms.EmailField(label=False, widget=forms.TextInput(attrs={"class": "form-control form-control-user","placeholder" : "Email Address ..."}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class": "form-control form-control-user","placeholder" : "Password..."}))
    confirm_password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class": "form-control form-control-user","placeholder" : "Confirm Password..."}))

class LoginForm(forms.Form):
    username = forms.CharField(label=False ,max_length=255 , widget=forms.TextInput(attrs={"class": "form-control form-control-user","placeholder" : "Enter Username..."}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={"class": "form-control form-control-user","placeholder" : "Enter Password..."}))
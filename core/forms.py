from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'item-user', 'placeholder': 'Insira seu nome de usuário'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'item', 'id': 'item-email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'item-user-password', 'placeholder': 'Insira sua senha'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'item-user', 'id': 'item-confirm-password'})
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este endereço de email já está em uso.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "As senhas não coincidem. Por favor, tente novamente."
            )


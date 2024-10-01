from django.db import models
from django.contrib.auth.models import User
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'item', 'id': 'item-login'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'item', 'id': 'item-login'})
    )


class Genero(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Musica(models.Model):
    titulo = models.CharField(max_length=255)
    artista = models.CharField(max_length=255)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    popularidade = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lista_musica = models.ManyToManyField(Musica)


class Recomendacao(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    musicas_recomendadas = models.ManyToManyField(Musica)


from django.shortcuts import render
from .models import LoginForm, Musica
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.db.models import Q
from .models import PerfilUsuario


def index(request):
    return render(request, 'index.html')



@login_required
def home(request):
    return render(request, 'home.html')


def musicas(request):
    query = request.GET.get('q')

    if query:
        results = Musica.objects.filter( Q(titulo__icontains=query) | Q(artista__icontains=query) | Q(genero__nome__icontains=query))
    else:
        results = Musica.objects.all();
    return render(request, 'musicas.html',  {'results': results})


def cadastrar(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)

            perfil = PerfilUsuario(user=user)

            perfil.save()

            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = RegistrationForm()
    return render(request, 'registration/cadastrar.html', {'form': form})
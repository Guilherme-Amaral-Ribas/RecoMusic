from django.urls import path
from .views import index, cadastrar, home, musicas


urlpatterns = [
    path('', index, name='index'),
    path('cadastrar', cadastrar, name='cadastrar'),
    path('home', home, name='home'),
    path('musicas', musicas, name='musicas'),

]

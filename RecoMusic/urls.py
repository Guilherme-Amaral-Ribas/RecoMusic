from django.contrib import admin
from django.urls import path, include

app_name = 'login'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('core.urls')),
]

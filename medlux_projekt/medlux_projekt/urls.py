"""
URL configuration for medlux_projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from accounts import views
urlpatterns = [
    path("pracownicy/", include("pracownicy.urls")), # url do bazy pracownikow
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  #url do logowania
    path("login/", views.login_view , name='login'),
    path('login/Dyrektor/', views.dyr_view, name='Dyrektor'),
    path('login/CEO/', views.CEO_view, name='CEO'),
    path('login/HR/', views.HR_view, name='HR'),
    path('login/Ksiegowa/', views.Ksiegowa_view, name='Ksiegowa'),
    path('login/Pracownik/', views.Pracownik_view, name='Pracownik'),
    path('login/Recepcja/', views.Recepcja_view, name='Recepcja'),
    path('login/Zaopatrzenie/', views.Zaopatrzenie_view, name='Zaopatrzenie'),
]

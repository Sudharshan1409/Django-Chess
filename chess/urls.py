"""OwnCloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePage, UserProfile
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('game.urls',namespace='game')),
    path('user/login/', auth_views.LoginView.as_view(), name='login'),
    path('user/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/signup/',views.RegisterUserPage.as_view(),name = 'signup'),
    path('user/profile/', UserProfile.as_view(), name='profile'),
    path('', HomePage.as_view(),name = 'home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

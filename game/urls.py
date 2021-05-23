from django.urls import path
import json
from . import views
app_name = 'game'

obj = {
    'hi': 'hello',
    'hey': 'yo'
}

urlpatterns = [
    path('selectopponent/', views.GamesList.as_view(), name='gamelist'),
    path('creategame/<int:pk>/', views.CreateGame.as_view(), name='creategame'),
    path('game/<int:pk>/', views.Game.as_view(), name='game'),
]

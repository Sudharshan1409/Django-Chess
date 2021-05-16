from django.urls import path
from . import views
app_name = 'game'

urlpatterns = [
    path('games/', views.GamesList.as_view(), name='gamelist'),
    path('new_game/', views.NewGame.as_view(), name='newgame')
]

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    player_white = models.ForeignKey(User, related_name='games_white', on_delete=models.SET_NULL, null=True)
    player_black = models.ForeignKey(User, related_name='games_black', on_delete=models.SET_NULL, null=True)
    winner = models.ForeignKey(User, related_name='wins', on_delete=models.SET_NULL, null=True)
    
    def get_absolute_url(self):
        return reverse('users:home',kwargs = {'pk':self.pk})

    def __str__(self):
        return f"{self.user.username.capitalize()} Profile"

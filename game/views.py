from django.views.generic import TemplateView

class GamesList(TemplateView):
    template_name = 'game/gamelist.html'

class NewGame(TemplateView):
    template_name = 'game/newgame.html'

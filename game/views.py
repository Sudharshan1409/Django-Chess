from django.views.generic import ListView, View, DetailView
from django.shortcuts import redirect
from game.models import Game as GameModel
import json
from django.contrib.auth.models import User as UserModel
import random

class GamesList(ListView):

    model = UserModel
    template_name = 'game/gamelist.html'

class CreateGame(View):

    def getPonsPositions(self):
        positions = {
            "a1": "white,rook", "b1": "white,knight", "c1": "white,bishop", "d1": "white,queen", "e1": "white,king", "f1": "white,bishop", "g1": "white,knight", "h1": "white,rook",
            "a2": "white,soldier", "b2": "white,soldier", "c2": "white,soldier", "d2": "white,soldier", "e2": "white,soldier", "f2": "white,soldier", "g2": "white,soldier", "h2": "white,soldier",
            "a3": "", "b3": "", "c3": "", "d3": "", "e3": "", "f3": "", "g3": "", "h3": "",
            "a4": "", "b4": "", "c4": "", "d4": "", "e4": "", "f4": "", "g4": "", "h4": "",
            "a5": "", "b5": "", "c5": "", "d5": "", "e5": "", "f5": "", "g5": "", "h5": "",
            "a6": "", "b6": "", "c6": "", "d6": "", "e6": "", "f6": "", "g6": "", "h6": "",
            "a7": "black,soldier", "b7": "black,soldier", "c7": "black,soldier", "d7": "black,soldier", "e7": "black,soldier", "f7": "black,soldier", "g7": "black,soldier", "h7": "black,soldier",
            "a8": "black,rook", "b8": "black,knight", "c8": "black,bishop", "d8": "black,queen", "e8": "black,king", "f8": "black,bishop", "g8": "black,knight", "h8": "black,rook"
        }
        return positions

    def get(self, request, *args, **kwargs):
        selected_user = UserModel.objects.get(id=kwargs['pk'])
        print('selected_user', selected_user)
        print('kwargs:', kwargs)
        decider = [
            {
                "player_white": request.user,
                "player_black": selected_user,
            },
            {
                "player_white": selected_user,
                "player_black": request.user,
            }
        ]
        color_decided = random.choice(decider)

        if color_decided['player_white'] == request.user:
            toggle = False
        else:
            toggle = True
            
        new_game = GameModel.objects.create(player_white=color_decided['player_white'], player_black=color_decided['player_black'], pons_position=self.getPonsPositions(), toggle_board=toggle)
        print(new_game)
        return redirect('game:game', pk = new_game.pk)

class Game(DetailView):
    model = GameModel
    template_name = 'game/game.html'
    context_object_name = 'game_details'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['dumps'] = json.dumps
        return context

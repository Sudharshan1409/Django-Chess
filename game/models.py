from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

def generate_pons_details():
    pons_details = {
        "black": {
            "rook": "♜",
            "knight": "♞",
            "bishop": "♝",
            "queen": "♛",
            "king": "♚",
            "soldier": "♟"
        },
        "white": {
            "rook": "♖",
            "knight": "♘",
            "bishop": "♗",
            "queen": "♕",
            "king": "♔",
            "soldier": "♙"
        }
    }
    return pons_details

def generate_king_positions():
    return {
        'black': 'e8',
        'white': 'e1'
    }

def generate_pon_status():
    pon_status = {
        'black_king_moved': False,
        'black_rook_moved_a8': False,
        'black_rook_moved_h8': False,
        'black_castling': False,
        'white_king_moved': False,
        'white_rook_moved_a1': False,
        'white_rook_moved_h1': False,
        'white_castling': False
    }
    return pon_status

def generate_moved_checks():
    return {
        'black': {
            'king': False,
            'rook': {
                'a': False,
                'h': False,
            },
            'castling': False,
        },
        'white': {
            'king': False,
            'rook': {
                'a': False,
                'h': False,
            },
            'castling': False,
        }
    }
    
def generate_movable_positions_pos():
    return {
        'a1': [],
        'b1': [ 'c3', 'a3' ],
        'c1': [],
        'd1': [],
        'e1': [],
        'f1': [],
        'g1': [ 'h3', 'f3' ],
        'h1': [],
        'a2': [ 'a3', 'a4' ],
        'b2': [ 'b3', 'b4' ],
        'c2': [ 'c3', 'c4' ],
        'd2': [ 'd3', 'd4' ],
        'e2': [ 'e3', 'e4' ],
        'f2': [ 'f3', 'f4' ],
        'g2': [ 'g3', 'g4' ],
        'h2': [ 'h3', 'h4' ]
        }

def generate_moves():
    return []

class Game(models.Model):
    player_white = models.ForeignKey(User, related_name='games_white', on_delete=models.SET_NULL, null=True)
    player_black = models.ForeignKey(User, related_name='games_black', on_delete=models.SET_NULL, null=True)
    winner = models.ForeignKey(User, related_name='wins', on_delete=models.SET_NULL, null=True)
    pons_position = models.JSONField(blank=True, null=True)
    pons_details = models.JSONField(default=generate_pons_details)
    turn = models.CharField(max_length=5, default='white')
    king_positions = models.JSONField(default=generate_king_positions)
    moved_checks = models.JSONField(default=generate_moved_checks)
    moves = models.JSONField(default=generate_moves)
    movable_positions_pos = models.JSONField(default=generate_movable_positions_pos)
    
    def get_absolute_url(self):
        return reverse('game:newgame',kwargs = {'pk':self.pk})

    # def __str__(self):
    #     return f"{self.user.username.capitalize()} Profile"



# Generated by Django 3.1.7 on 2021-05-30 17:27

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_remove_game_pon_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='movable_positions_pos',
            field=models.JSONField(default=game.models.generate_movable_positions_pos),
        ),
    ]

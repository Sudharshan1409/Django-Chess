# Generated by Django 3.1.7 on 2021-05-25 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_game_moves'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='pon_status',
        ),
    ]

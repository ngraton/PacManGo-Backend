from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()


class Player(models.Model):
  display_name = models.CharField(max_length=30, blank=True) 
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')


class Game(models.Model):
  winner = models.ForeignKey(Player, blank=True, null=True, related_name='games_won', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  center_lat = models.FloatField()
  center_lon = models.FloatField()
  zoom = models.IntegerField()
  players = models.ManyToManyField(
    'Player',
    through='Run_Map',
    related_name='games',
    blank=True,
  )

class Run_Map(models.Model):
  player = models.ForeignKey(Player, related_name='run_maps', on_delete=models.CASCADE)
  game = models.ForeignKey(Game, related_name='run_maps', on_delete=models.CASCADE)
  score = models.IntegerField()

class Route(models.Model):
  run_map = models.ForeignKey(Run_Map, related_name='routes', on_delete=models.CASCADE)

class Point(models.Model):
  lat = models.FloatField()
  lon = models.FloatField()
  route = models.ForeignKey(Route, related_name='points', on_delete=models.CASCADE)

# class Bounus(models.Model):
#   lat = models.FloatField()
#   lon = models.FloatField()
#   game = models.ForeignKey(Game, related_name='bonuses')




  

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


from .models import Player, Game, Run_Map, Route, Point

class PointSerializer(ModelSerializer):
  class Meta:
    model = Point
    fields = ('id', 'lat', 'lon', 'route')

class RouteSerializer(ModelSerializer):
  points = PointSerializer(many=True, read_only=True)
  class Meta:
    model = Route
    fields = ('id', 'run_map', 'points')

class Run_MapSerializer(ModelSerializer):
  routes = RouteSerializer(many=True, read_only=True)
  class Meta:
    model = Run_Map
    fields = ('id', 'player', 'game', 'routes', 'score')

class PlayerSerializer(ModelSerializer):
  # games = GameSerializer(many=True, allow_empty=True, read_only=True)
  user = serializers.SlugRelatedField(
    read_only=True,
    slug_field='username'
  )
  class Meta:
    model = Player
    fields = ('id', 'games', 'user')

class GameSerializer(ModelSerializer):
  run_maps = Run_MapSerializer(many=True, read_only=True)
  players = PlayerSerializer(many=True, read_only=True)
  class Meta:
    model = Game
    fields = ('id', 'winner', 'name', 'players', 'run_maps', 'center_lat', 'center_lon', 'zoom')
    # depth = 2

class TokenSerializer(ModelSerializer):
  class Meta:
    model = Token
    fields = ('key', 'user')
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from .serializers import PointSerializer, RouteSerializer, Run_MapSerializer, GameSerializer, PlayerSerializer
from .models import Player, Game, Run_Map, Route, Point


class PlayerViewSet(NestedViewSetMixin, ModelViewSet):
  serializer_class = PlayerSerializer
  queryset = Player.objects.all()

class GameViewSet(NestedViewSetMixin, ModelViewSet):
  serializer_class = GameSerializer
  queryset = Game.objects.all()
  
class Run_MapViewSet(NestedViewSetMixin, ModelViewSet):
  serializer_class = Run_MapSerializer
  queryset = Run_Map.objects.all()

class RouteViewSet(NestedViewSetMixin, ModelViewSet):
  serializer_class = RouteSerializer
  queryset = Route.objects.all()

class PointViewSet(NestedViewSetMixin, ModelViewSet):
  serializer_class = PointSerializer
  queryset = Point.objects.all()





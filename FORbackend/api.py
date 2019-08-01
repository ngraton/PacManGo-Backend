from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin
from FOR.views import PlayerViewSet, GameViewSet, RouteViewSet, Run_MapViewSet, PointViewSet

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
  pass

router = NestedDefaultRouter()
players_router = router.register('players', PlayerViewSet)
players_router.register(
  'games', GameViewSet,
  basename='player-games',
  parents_query_lookups=['players']
)
game_router = router.register('games', GameViewSet)
game_router.register(
  'players', PlayerViewSet,
  basename='game-players',
  parents_query_lookups=['games']
)
run_maps_router = router.register('run_maps', Run_MapViewSet)
run_maps_router.register(
  'routes', RouteViewSet,
  basename='run_map-routes',
  parents_query_lookups=['run_map']
)
routes_router = router.register('routes', RouteViewSet)
routes_router.register(
  'points', PointViewSet,
  basename='route_points',
  parents_query_lookups=['route']
)

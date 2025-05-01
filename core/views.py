from rest_framework import viewsets
from rest_framework.response import Response
from . import filters

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        precessing_time = filters.get_superusers()[1]
        timestamp = filters.active_users_per_day()[2]
        superusers = filters.get_superusers()[0]
        return Response({f'precessing_time': precessing_time, 'timestamp': timestamp, 'superusers': superusers})
    
class TopContries(viewsets.ViewSet):
    def list(self, request):
        precessing_time = filters.top_countries()[1]
        timestamp = filters.active_users_per_day()[2]
        top_countries = filters.top_countries()[0]
        return Response({f'precessing_time': precessing_time, 'timestamp': timestamp, 'top_countries': top_countries})
    
class TeamInsights(viewsets.ViewSet):
    def list(self, request):
        precessing_time = filters.team_insights()[1]
        timestamp = filters.active_users_per_day()[2]
        team_insights = filters.team_insights()[0]
        return Response({f'precessing_time': precessing_time, 'timestamp': timestamp, 'team_insights': team_insights})

class ActiveUsersByDay(viewsets.ViewSet):
    def list(self, request):
        precessing_time = filters.active_users_per_day()[1]
        timestamp = filters.active_users_per_day()[2]
        active_users_by_day = filters.active_users_per_day()[0]
        return Response({f'precessing_time': precessing_time, 'timestamp': timestamp, 'active_users_by_day': active_users_by_day})
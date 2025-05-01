from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=True)
router.register('superusers', views.UserViewSet, basename='superusers')
router.register('top-countries', views.TopContries, basename='countries')
router.register('team-insights', views.TeamInsights, basename='team-insights')
router.register('active-users-per-day', views.ActiveUsersByDay, basename='active-users-per-day')

urlpatterns = router.urls
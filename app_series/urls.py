from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'genders', views.GendersViewSet)
router.register(r'genders/(?P<pk>\d+)/series',
                views.GendersViewSet, basename='gender-series')
router.register(r'series', views.SeriesViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'episodes', views.EpisodesViewSet)
router.register(r'platforms', views.PlatformsViewSet)
router.register(r'platforms/(?P<pk>\d+)/series',
                views.PlatformsViewSet, basename='platform-series')

urlpatterns = [
    path('', include(router.urls)),
]

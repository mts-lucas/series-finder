from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'genders', views.GendersViewSet)
router.register(r'genders/(?P<pk>\d+)/series',
                views.GendersViewSet, basename='gender-series')

router.register(r'series', views.SeriesViewSet)
router.register(r'series/(?P<pk>\d+)/seasons',
                views.SeriesViewSet, basename='serie-seasons')
router.register(r'series/(?P<pk>\d+)/episodes',
                views.SeriesViewSet, basename='series-episodes')

router.register(r'seasons', views.SeasonViewSet)
router.register(r'seasons/(?P<pk>\d+)/episodes',
                views.SeasonViewSet, basename='season-episodes')

router.register(r'episodes', views.EpisodesViewSet)

router.register(r'platforms', views.PlatformsViewSet)
router.register(r'platforms/(?P<pk>\d+)/series',
                views.PlatformsViewSet, basename='platform-series')

urlpatterns = [
    path('', include(router.urls)),
]

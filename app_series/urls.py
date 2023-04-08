from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'genders', views.GendersViewSet)
router.register(r'series', views.SeriesViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'episodes', views.EpisodesViewSet)
router.register(r'platforms', views.PlatformsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('genders/int:<pk>/series/',
         views.GendersViewSet.as_view({'get': 'series'}),
         name='gender-series'),
    path('series/int:<pk>/seasons/',
         views.SeriesViewSet.as_view({'get': 'seasons'}),
         name='serie-seasons'),
    path('series/int:<pk>/episodes/',
         views.SeriesViewSet.as_view({'get': 'episodes'}),
         name='series-episodes'),
    path('seasons/int:<pk>/episodes/',
         views.SeasonViewSet.as_view(
             {'get': 'episodes'}), name='season-episodes'),
    path('platforms/int:<pk>/series/',
         views.PlatformsViewSet.as_view(
             {'get': 'series'}), name='platform-series'),
]

from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'genders', views.GendersViewSet)
router.register(r'series', views.SeriesViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'episodes', views.EpisodesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

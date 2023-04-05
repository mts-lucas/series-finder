from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('genders', views.GendersViewSet)
router.register('series', views.SeriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

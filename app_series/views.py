# O atributo permission_classes é uma lista de classes de permissão
# que serão aplicadas a todas as operações HTTP disponíveis na ViewSet.
# As classes de permissão mais comuns no Django REST framework incluem:

# AllowAny: permite que qualquer pessoa acesse o recurso (sem autenticação).
# IsAuthenticated: permite que apenas usuários autenticados acessem o recurso.
# IsAdminUser: permite que apenas usuários com privilégios
# de administrador acessem o recurso.
# IsAuthenticatedOrReadOnly: permite que usuários autenticados
# façam alterações no recurso, enquanto usuários não autenticados
# podem apenas visualizá-lo (leitura).

from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Episode, Gender, Platform, Season, Serie
from .serializers import (EpisodeSerializer, GenderSerializer,
                          PlatformSerializer, SeasonSerializer,
                          SerieSerializer)


class PlatformsViewSet(viewsets.ModelViewSet):

    queryset = Platform.objects.all().order_by('name')
    serializer_class = PlatformSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def series_list(self, request, pk=None):
        platform = self.get_object()
        series = Serie.objects.filter(platforms=platform)
        serializer = SerieSerializer(
            series, many=True, context={'request': request})
        return Response(serializer.data)


class GendersViewSet(viewsets.ModelViewSet):

    queryset = Gender.objects.all().order_by('name')
    serializer_class = GenderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def series_list(self, request, pk=None):
        gender = self.get_object()
        series = Serie.objects.filter(genders=gender)
        serializer = SerieSerializer(
            series, many=True, context={'request': request})
        return Response(serializer.data)


class SeriesViewSet(viewsets.ModelViewSet):

    queryset = Serie.objects.all().order_by('title')
    serializer_class = SerieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def seasons_list(self, request, pk=None):
        serie = self.get_object()
        seasons = serie.seasons.all()
        serializer = SeasonSerializer(
            seasons, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def episodes_list(self, request, pk=None):
        serie = self.get_object()
        episodes = Episode.objects.filter(
            season__serie=serie).order_by('season__number', 'number')
        serializer = EpisodeSerializer(
            episodes, many=True, context={'request': request})
        return Response(serializer.data)


class EpisodesViewSet(viewsets.ModelViewSet):

    queryset = Episode.objects.all().order_by('season__serie', 'number')
    serializer_class = EpisodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SeasonViewSet(viewsets.ModelViewSet):

    queryset = Season.objects.all().order_by('serie', 'number')
    serializer_class = SeasonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def episodes_list(self, request, pk=None):
        season = self.get_object()
        episodes = season.episodes.all()
        serializer = EpisodeSerializer(
            episodes, many=True, context={'request': request})
        return Response(serializer.data)

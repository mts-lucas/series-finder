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

from .models import Episode, Gender, Platform, Season, Serie
from .serializers import (EpisodeSerializer, GenderSerializer,
                          PlatformSerializer, SeasonSerializer,
                          SerieSerializer)


class PlatformsViewSet(viewsets.ModelViewSet):

    queryset = Platform.objects.all().order_by('name')
    serializer_class = PlatformSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GendersViewSet(viewsets.ModelViewSet):

    queryset = Gender.objects.all().order_by('name')
    serializer_class = GenderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SeriesViewSet(viewsets.ModelViewSet):

    queryset = Serie.objects.all().order_by('title')
    serializer_class = SerieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EpisodesViewSet(viewsets.ModelViewSet):

    queryset = Episode.objects.all().order_by('season__serie', 'number')
    serializer_class = EpisodeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SeasonViewSet(viewsets.ModelViewSet):

    queryset = Season.objects.all().order_by('serie', 'number')
    serializer_class = SeasonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

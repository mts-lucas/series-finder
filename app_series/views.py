# Endpoint de busca - Permitir aos usuários
# pesquisar por séries pelo nome ou gênero.

# Endpoint de detalhes da série - Fornecer informações
# sobre uma série específica, como enredo, datas de lançamento,
# bem como a disponibilidade em diferentes plataformas de streaming.

# Endpoint de episódios - Listar episódios de uma série,
# incluindo informações sobre o título do episódio,
# sinopse, duração, data de lançamento.

# Endpoint de gêneros - Permitir que os usuários pesquisem por séries
# por gênero, incluindo comédia, drama, terror, ação, etc.

# Endpoint de plataforma de streaming - Listar as plataformas
# de streaming onde uma série está disponível

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

# class GenderSeriesViewSet(APIView):

#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     serializer_class = SerieSerializer

#     def get_queryset(self):

#         queryset = Serie.objects.all()
#         gender_name = self.request.query_params.get('gender', None)
#         if gender_name is not None:
#             queryset = queryset.filter(genders__name=gender_name)
#         else:
#             return Response(
#                 {'error': 'Please, insert a valid id for your request.'},
#                 status=status.HTTP_400_BAD_REQUEST)
#         return queryset

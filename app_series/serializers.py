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


from rest_framework import serializers

from .models import Episode, Gender, Season, Serie


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

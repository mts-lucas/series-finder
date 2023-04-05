from rest_framework import serializers

from .models import Episode, Gender, Season, Serie


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Season
        fields = '__all__'


class SerieSerializer(serializers.HyperlinkedModelSerializer):
    seasons = SeasonSerializer(many=True, read_only=True)
    genders = GenderSerializer(many=True, read_only=True)

    class Meta:
        model = Serie
        fields = '__all__'

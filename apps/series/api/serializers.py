from rest_framework import serializers

from apps.gallery.api.serializers import ImageSerializer

from .. import models


class EpisodeShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Episode
        fields = (
            'id',
            'title',
        )


class EpisodeSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True)

    class Meta:
        model = models.Episode
        fields = (
            'id',
            'title',
            'images',
        )


class SeriesShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Series
        fields = (
            'id',
            'title',
        )


class SeriesSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True)
    episodes = EpisodeShortSerializer(many=True)

    class Meta:
        model = models.Series
        fields = (
            'id',
            'title',
            'description',
            'images',
            'episodes',
        )

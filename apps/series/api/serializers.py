from rest_framework import serializers

from apps.gallery.api.serializers import ImageSerializer

from .. import models


class SeriesShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Series
        fields = (
            'id',
            'title',
        )


class SeriesSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True)

    class Meta:
        model = models.Series
        fields = (
            'id',
            'title',
            'description',
            'images',
        )

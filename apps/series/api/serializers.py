from rest_framework import serializers

from .. import models


class SeriesShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Series
        fields = (
            'id',
            'title',
        )


class SeriesSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.Series
        fields = (
            'id',
            'title',
            'description',
        )

from rest_framework import serializers

from .. import models


class ImageSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()

    class Meta:
        model = models.Image
        fields = (
            'url',
        )

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(
            obj.image.url,
        )

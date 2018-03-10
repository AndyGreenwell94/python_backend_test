from rest_framework import viewsets, mixins

from . import serializers
from .. import models


class SeriesViewset(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = models.Series.objects.all()
    serializer_class = serializers.SeriesSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.SeriesShortSerializer
        return super().get_serializer_class()

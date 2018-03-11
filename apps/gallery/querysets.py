from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet


class ImageQuerySet(QuerySet):

    def get_for_object(self, obj):
        return self.filter(
            content_type=ContentType.objects.get_for_model(obj),
            object_id=obj.id,
        )

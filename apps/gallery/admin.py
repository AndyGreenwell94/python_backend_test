from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline


from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'content_type',
        'object_id',
    )


class ImageInlineAdmin(GenericTabularInline):
    model = models.Image

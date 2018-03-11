from django.contrib import admin

from apps.gallery.admin import ImageInlineAdmin

from . import models


@admin.register(models.Series)
class SeriesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
    )

    inlines = (
        ImageInlineAdmin,
    )


@admin.register(models.Episode)
class EpisodeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'series',
    )

    inlines = (
        ImageInlineAdmin,
    )

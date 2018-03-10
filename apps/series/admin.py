from django.contrib import admin

from . import models


@admin.register(models.Series)
class SeriesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
    )

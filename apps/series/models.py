from django.db import models

from apps.gallery.mixins import ImageRelationMixin


class Series(ImageRelationMixin,
             models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name='Series title',
        help_text='Title of the series',
    )
    description = models.TextField(
        verbose_name='Series description',
        help_text='Description of the series',
    )

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return f'<Series {self.id}: {self.title}>'


class Episode(ImageRelationMixin,
              models.Model):

    series = models.ForeignKey(
        to=Series,
        on_delete=models.CASCADE,
        related_name='episodes',
        verbose_name='Episodes Series',
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Episode title',
    )

    def __str__(self):
        return f'<Episode if {self.series.title} {self.id}: {self.title}>'

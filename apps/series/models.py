from django.db import models


class Series(models.Model):

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

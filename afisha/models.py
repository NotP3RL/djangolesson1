from django.db import models


class Place(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    short_description = models.TextField('Короткое название')
    long_description = models.TextField('Длинное описание', blank=True)
    lng = models.FloatField('Долгота')
    lat = models.FloatField('Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def str(self):
        return f'{self.title}'

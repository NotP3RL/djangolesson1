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

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    ordinal_number = models.IntegerField('Номер', default=0, db_index=True)
    image = models.ImageField('Изображение')
    place = models.ForeignKey(Place, related_name='images', verbose_name='Место', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['ordinal_number']

    def __str__(self):
        return f'{self.place.title}'

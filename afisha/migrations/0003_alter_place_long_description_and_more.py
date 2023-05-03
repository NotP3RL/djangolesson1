# Generated by Django 4.1.7 on 2023-05-03 10:16

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0002_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Длинное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=tinymce.models.HTMLField(verbose_name='Короткое название'),
        ),
    ]

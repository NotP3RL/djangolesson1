# Generated by Django 4.1.7 on 2023-05-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0003_alter_place_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(verbose_name='Короткое название'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0004_alter_place_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Короткое название'),
        ),
    ]
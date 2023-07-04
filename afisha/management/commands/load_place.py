from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import requests
from afisha.models import Place, Image


class Command(BaseCommand):
    help = 'Загружает данные о месте в БД'

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        response_content = response.json()
        place, created = Place.objects.get_or_create(
            title=response_content['title'],
            lng=response_content['coordinates']['lng'],
            lat=response_content['coordinates']['lat'],
            defaults={'short_description': response_content['description_short'],
                      'long_description': response_content['description_long']}
        )
        if not created:
            return
        for number, image_url in enumerate(response_content['imgs']):
            try:
                response = requests.get(image_url)
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                continue
            image = Image.objects.create(
                ordinal_number=number,
                image=ContentFile(response.content, name=f'{place.title} {number}'),
                place=place
            )

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            help='Ссылка на json с данными'
        )

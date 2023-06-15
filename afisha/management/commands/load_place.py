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
            title=response_content.get('title', []),
            short_description=response_content.get('description_short', []),
            long_description=response_content.get('description_long', []),
            lng=response_content['coordinates'].get('lng', []),
            lat=response_content['coordinates'].get('lat', [])
        )
        if not created:
            return
        for number, image_url in enumerate(response_content['imgs']):
            try:
                response = requests.get(image_url)
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                continue
            image, _ = Image.objects.get_or_create(
                ordinal_number=number,
                image=ContentFile(response.content, name=f'{place.title} {number}'),
                place=place
            )

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            help='Ссылка на json с данными'
        )

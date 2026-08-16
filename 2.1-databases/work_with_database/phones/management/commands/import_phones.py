import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            try:
                obj = Phone(
                id=phone.get('id'),
                name = phone.get('name'),
                slug = phone.get('slug'),
                image = phone.get('image'),
                price = float(phone.get('price')),
                release_date = phone.get('release_date'),
                lte_exists = bool(phone.get('lte_exists'))
            )
                obj.save()
            except:
                continue
    

        

        


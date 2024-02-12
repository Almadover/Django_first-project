import csv
import re
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

            for row in phones:
                phone = Phone()
                phone.name = row['name']
                phone.image = row['image']
                phone.price = row['price']
                phone.release_date = row['release_date']
                phone.lte_exists = row['lte_exists']
                phone.slug = slugify(row['name'])

                phone.save()
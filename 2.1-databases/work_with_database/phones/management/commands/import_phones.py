import csv

from django.core.management.base import BaseCommand
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
            phone.price = row['price']
            phone.image = row['image']
            phone.release_date = ['release_date']
            phone.lte_exists = ['lte_exists']
            phone.save()

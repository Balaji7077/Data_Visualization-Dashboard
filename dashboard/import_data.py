import json
from django.core.management.base import BaseCommand
from dashboard.models import Data

class Command(BaseCommand):
    help = 'Load data from jsondata.json'

    def handle(self, *args, **kwargs):
        with open("C:\Users\lookz\OneDrive\Desktop\django project\balaji\Scripts\mydashboard\dashboard\jsondata.json",'r') as f:
            data = json.load.read(f)
            for item in data:
                Data.objects.create(
                    intensity=item.get('intensity'),
                    likelihood=item.get('likelihood'),
                    relevance=item.get('relevance'),
                    year=item.get('year'),
                    country=item.get('country'),
                    topic=item.get('topic'),
                    region=item.get('region'),
                    city=item.get('city')
                )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))




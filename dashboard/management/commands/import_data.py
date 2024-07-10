from django.core.management.base import BaseCommand
import json
from dashboard.models import Data

class Command(BaseCommand):
    help = 'Import data from JSON file'

    def handle(self, *args, **kwargs):
        json_file_path = r"C:\Users\lookz\OneDrive\Desktop\django project\balaji\Scripts\mydashboard\dashboard\jsondata.json"
        
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.stdout.write(f'Successfully loaded JSON data: {data}')
                
                for item in data:
                    try:
                        # Validate numeric fields
                        intensity = float(item.get('intensity', 0))  # Replace with default value if missing
                        likelihood = float(item.get('likelihood', 0))
                        relevance = float(item.get('relevance', 0))
                        
                        # Validate and convert year
                        year = int(item['year']) if 'year' in item and item['year'] is not None else None
                        if year is None:
                            raise ValueError('Year is missing or invalid')
                        
                        city = int(item['city']) if 'city' in item and item['city'] is not None else None
                        if city is None:
                            raise ValueError('City is missing')
                        
                        Data.objects.create(
                            intensity=intensity,
                            likelihood=likelihood,
                            relevance=relevance,
                            year=year,
                            country=item.get('country'),
                            topic=item.get('topic'),
                            region=item.get('region'),
                            city=city,
                        )
                        self.stdout.write(f'Successfully imported data for {item["city"]}')
                    
                    except ValueError as ve:
                        self.stderr.write(f'Error creating object for {item["city"]}: {ve}')
                
                self.stdout.write('Data import process completed.')
                
        except FileNotFoundError:
            self.stderr.write(f'File not found at path: {json_file_path}')
        except json.JSONDecodeError as e:
            self.stderr.write(f'Error decoding JSON: {str(e)}')
        except UnicodeDecodeError as e:
            self.stderr.write(f'Error decoding Unicode: {str(e)}. Try using "utf-8" encoding instead.')

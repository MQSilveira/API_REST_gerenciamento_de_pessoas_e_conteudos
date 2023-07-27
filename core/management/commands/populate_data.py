import json
from django.core.management.base import BaseCommand
from core.models import Person, Content


class Command(BaseCommand):
    help = 'Populate database with data from data.json file'

    def handle(self, *args, **kwargs):
        with open('data.json') as file:
            data = json.load(file)

        people_data = data.get('people', [])
        content_data = data.get('content', [])

        people_instances = []  # List to store the instances of Person

        # Create and save instances of Person
        for person_item in people_data:
            person = Person.objects.create(name=person_item['name'])
            self.stdout.write(self.style.SUCCESS(f'Successfully created Person: {person.name}'))
            people_instances.append(person)  # Adds the Person instance to the list

        # Create and save instances of Content with different creators
        for idx, content_item in enumerate(content_data):
            creator = people_instances[idx % len(people_instances)]  # Use module to select different breeders
            content = Content.objects.create(text=content_item['text'], creator=creator)
            content.read_by.set(people_instances)  # Add all instances of Person to the "read_by" field
            self.stdout.write(self.style.SUCCESS(f'Successfully created Content: {content.text}'))

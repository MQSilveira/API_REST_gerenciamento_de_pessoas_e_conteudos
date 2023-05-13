from core.models import Content, Person

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json


@csrf_exempt
def load_data(request):
    
    with open('data.json') as js:
        objeto = json.load(js)

    people = []
    objeto = zip(objeto['people'], objeto['content'])
    
    for objeto_person, objeto_content in objeto:
        
        person = Person(name=objeto_person['name'])
        people.append(person)
        person.save()

        content = Content(text=objeto_content['text'], creator=person)
        content.save()


    objeto_content = Content.objects.all()
    
    for content in objeto_content:
        content.read_by.set(people)
        
    return HttpResponse("Dados carregados com sucesso!")


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from core.models import Person


class PersonTests(APITestCase):
    def setUp(self):
        self.url = reverse('person-list')
        self.data = {'name': 'John Doe'}
        self.person = Person.objects.create(name='Jane Doe')

    def test_create_person(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)

    def test_get_person_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_person_detail(self):
        url = reverse('person-detail', kwargs={'pk': self.person.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Jane Doe')

    def test_update_person(self):
        url = reverse('person-detail', kwargs={'pk': self.person.pk})
        data = {'name': 'Jane Smith'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Person.objects.get(pk=self.person.pk).name, 'Jane Smith')

    def test_delete_person(self):
        url = reverse('person-detail', kwargs={'pk': self.person.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
        

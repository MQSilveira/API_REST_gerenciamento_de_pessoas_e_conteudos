from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Content(models.Model):
    text = models.TextField(max_length=200)
    creator = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='contents_created')
    read_by = models.ManyToManyField(Person, related_name='contents_read')

    def __str__(self):
        return self.text

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import get_object_or_404 

from . serializers import PersonSerializer, ContentSerializer
from . serializers import ContentCreateSerializer, ContentUpdateSerializer

from core.models import Person, Content


class Pagination(PageNumberPagination):
    page_size = 50

## Content ##
class ContentViewset(viewsets.ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()
    pagination_class = Pagination
    
    def get_serializer_class(self):
        
        if self.action == 'create':
            return ContentCreateSerializer
        
        elif self.action == 'update':
            return ContentUpdateSerializer
    
        return ContentSerializer
    
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        queryset = instance.read_by.values('id', 'name')
        
        readers = [{'id': reader['id'], 'name': reader['name']} for reader in queryset]
        
        serializer = self.get_serializer(instance)
        content_data = serializer.data
        content_data['read_by'] = readers
        
        return Response(content_data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response(status=status.HTTP_200_OK)
    
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            allowed_fields = {'text', 'creator'}
            for field in request.data.keys():
                if field not in allowed_fields:
                    serializer.validated_data.pop(field, None)

            self.perform_update(serializer)
            return Response(serializer.data)
        
        else:
            return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def mark_as_read(self, request, content_pk=None, person_pk=None):
        content = get_object_or_404(Content, pk=content_pk)
        person = get_object_or_404(Person, pk=person_pk)
        content.read_by.add(person)
        
        return Response({'status': 'success'})
## FIM Content ##


## Person ##
class PersonViewset(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        
        for person in serializer.data:
            person['contents_created'] = list(Content.objects.filter(creator_id=person['id']).values('id', 'text'))
            
        return self.get_paginated_response(serializer.data)
    
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        contents_created = list(Content.objects.filter(creator_id=instance.id).values('id', 'text'))
        serializer_data = serializer.data
        serializer_data['contents_created'] = contents_created

        return Response(serializer_data)


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        
        return Response(status=status.HTTP_200_OK)
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        
        else:
            return Response({"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
## FIM Person ##

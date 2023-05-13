from rest_framework import serializers
from core.models import Person, Content


class PersonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ['id', 'name']      
        
       
class ContentSerializer(serializers.ModelSerializer):
    read_by = PersonSerializer(many=True)
    
    class Meta:
        model = Content
        fields = ['id', 'text', 'read_by']
        

class ContentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Content
        fields = ['text', 'creator', 'read_by']

    def create(self, validated_data):
        read_by = validated_data.pop('read_by')
        content = Content.objects.create(**validated_data)
        
        for person in read_by:
            content.read_by.add(person)
            
        return content
    
    
class ContentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['text', 'creator']
    

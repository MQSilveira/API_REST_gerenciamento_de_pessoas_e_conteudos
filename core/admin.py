from django.contrib import admin
from . models import Person, Content


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'creator']


admin.site.register(Person, PersonAdmin)
admin.site.register(Content, ContentAdmin)

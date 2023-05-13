from django.urls import path, include

from rest_framework import routers
from core.api.viewset import PersonViewset, ContentViewset
from core.api.load_data import load_data


route = routers.DefaultRouter()

route.register(r'people', PersonViewset, basename='Person')
route.register(r'content', ContentViewset, basename='Content')


urlpatterns = [
    path('', include(route.urls)),
    path('content/<int:content_pk>/<int:person_pk>/mark-as-read/', 
         ContentViewset.as_view({'post':'mark_as_read'}), name='mark_as_read'),
    path('load-data/', load_data, name='load_data'),
]

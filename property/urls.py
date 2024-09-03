from django.urls import path
from . import api

urlpatterns = [
    path('', api.PropertiesListView.as_view(), name='api_properties_list'),
    path('create/', api.PropertyCreateView.as_view(), name='api_properties_create'),
]
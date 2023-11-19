from django.urls import path
from .views import get_data_and_store

urlpatterns = [
    path('fetch/', get_data_and_store, name='get_data_and_store'),
]
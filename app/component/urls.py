from .views import get_user_details
from django.urls import path

urlpatterns = [
    path('profile/', get_user_details)
]

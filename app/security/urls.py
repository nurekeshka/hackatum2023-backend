from django.urls import path
from .views import ObtainJWTToken
urlpatterns = [
    path('token/', ObtainJWTToken.as_view(), name='token_obtain'),
    # path('token/refresh/', ObtainJWTToken.as_view(), name='token_obtain'),
    # Add other URL patterns as needed
]
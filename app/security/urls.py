from django.urls import path
from .views import ObtainJWTToken, get_token_data, remove_token_data
urlpatterns = [
    path('token/', ObtainJWTToken.as_view(), name='token_obtain'),
    path('get_token_data/', get_token_data, name='get_token_data'),
    path('remove_token_data/', remove_token_data, name='remove_token_data'),
    # path('token/refresh/', ObtainJWTToken.as_view(), name='token_obtain'),
    # Add other URL patterns as needed
]
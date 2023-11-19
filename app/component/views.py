from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
def user_info(request):
    user=User.objects.all()
    serializer=UserSerializer(user, many=True)
    return JsonResponse(serializer)

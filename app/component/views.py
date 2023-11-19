from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_user_details(request):
    try:
        user = User.objects.get(id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)

    serializer = UserSerializer(user)
    return Response(serializer.data)
# def user_info(request):
#     user = User.objects.all()
#     serializer=UserSerializer(user)
#     return JsonResponse(serializer)

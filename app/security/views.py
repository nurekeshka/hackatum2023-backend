from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Security

class ObtainJWTToken(APIView):
    def post(self, request, *args, **kwargs):
        username = request.GET.get('username')
        password = request.GET.get('password')

        if username is None or password is None:
            return Response(status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            request.session['current_token_data'] = {'key': token.key}
            Security.session_token = token.key
            return Response({"token": token.key})
        else:
            return Response(status=400)


@api_view(['GET'])
def get_token_data(request):
    # Retrieving data from the session
    current_token_data = request.session.get('current_token_data', {})

    return JsonResponse(current_token_data)


@api_view(['GET'])
def remove_token_data(request):
    # Removing data from the session
    if 'current_token_data' in request.session:
        current_token_data = request.session.get('current_token_data', {})

        del request.session['current_token_data']
    return HttpResponse("Token data removed successfully.")


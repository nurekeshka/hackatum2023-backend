from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class ObtainJWTToken(APIView):
    def post(self, request, *args, **kwargs):
        username = request.GET.get('username')
        password = request.GET.get('password')

        if username is None or password is None:
            return Response(status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response(status=400)


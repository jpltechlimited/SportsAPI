from django.contrib.auth import authenticate
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.views import APIView
from .models import *
from .serializers import TennisPlayerSerializer
from rest_framework.authtoken.models import Token


class TennisPlayerAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    tennis_players = TennisPlayer.objects

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = TennisPlayerSerializer(snippet)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return self.tennis_players.get(pk=pk)
        except TennisPlayer.DoesNotExist:
            raise Http404


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def get_token(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)

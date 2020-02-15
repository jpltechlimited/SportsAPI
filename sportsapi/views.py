from django.contrib.auth import authenticate
from django.http import Http404
from django.shortcuts import render
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


#class TennisPlayerAPIView(APIView):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication, SessionAuthentication)
    #tennis_players = TennisPlayer.objects

    #def get(self, request, pk):
        #snippet = self.get_object(pk)
        #serializer = TennisPlayerSerializer(snippet)
        #return Response(serializer.data)

    #def get_object(self, pk):
        #try:
            #return self.tennis_players.get(pk=pk)
        #except TennisPlayer.DoesNotExist:
            #raise Http404

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import TennisPlayerSerializer


class TennisPlayerAPIView(APIView):
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

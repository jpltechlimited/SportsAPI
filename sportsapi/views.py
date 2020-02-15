from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class TennisPlayerAPIView(APIView):
    tennis_players = TennisPlayer.objects

    def get_object(self, pk):
        try:
            return self.tennis_players.get(pk=pk)
        except TennisPlayer.DoesNotExist:
            raise Http404

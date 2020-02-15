from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *


class TennisPlayerViewSet(viewsets.ModelViewSet):
    serializer_class = TennisPlayerSerializer
    queryset = TennisPlayer.objects.all()

    def retrieve(self, request, pk=None):
        players = TennisPlayer.objects.all()
        serializer = self.get_serializer(players, many=True)
        return Response(serializer.data)

    def list(self, request):
        pass

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

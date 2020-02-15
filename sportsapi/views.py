from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class TennisPlayerAPI(viewsets.ModelViewSet):
    serializer_class = TennisPlayerSerializer
    queryset = TennisPlayer.objects.all()

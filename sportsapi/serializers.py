from rest_framework import serializers
from .models import *


class TennisPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TennisPlayer
        fields = "__all__"

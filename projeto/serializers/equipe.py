from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField

from projeto.models import Equipe


class EquipeSerializer(ModelSerializer):
    user = StringRelatedField(many=True)

    class Meta:
        model = Equipe
        fields = ("id", "data", "user")
        depth = 1

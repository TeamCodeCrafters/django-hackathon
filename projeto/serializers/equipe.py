from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField

from projeto.models import Equipe


class EquipeSerializer(ModelSerializer):
    class Meta:
        model = Equipe
        fields = '__all__'
        depth = 1

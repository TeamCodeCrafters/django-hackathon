# serializers.py
from rest_framework import serializers
from ..models import EquipeAnalise

class EquipeAnaliseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipeAnalise
        fields = '__all__'

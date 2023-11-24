from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from projeto.models import Equipe
from projeto.serializers import EquipeSerializer

class EquipeViewSet(ModelViewSet):  
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    queryset = Equipe.objects.all().order_by("-data")
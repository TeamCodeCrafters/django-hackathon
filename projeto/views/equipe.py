from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated

from projeto.models import Equipe
from projeto.serializers import EquipeSerializer


class EquipeViewSet(ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [IsAuthenticated]

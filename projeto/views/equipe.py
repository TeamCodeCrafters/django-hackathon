from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import render, redirect
from projeto.models import EquipeForm

from projeto.models import Equipe
from projeto.serializers import EquipeSerializer


class EquipeViewSet(ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer


def criar_equipe(request):
    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            equipe = form.save()
            return redirect("sucesso")
    else:
        form = EquipeForm()

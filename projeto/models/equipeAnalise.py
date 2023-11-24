# models.py
from django.db import models
from django.shortcuts import redirect
from .equipe import Equipe


class EquipeAnalise(models.Model):
    nome = models.CharField(max_length=100)
    integrante1 = models.CharField(max_length=100, blank=True)
    integrante2 = models.CharField(max_length=100, blank=True)
    integrante3 = models.CharField(max_length=100, blank=True)
    integrante4 = models.CharField(max_length=100, blank=True)
    integrante5 = models.CharField(max_length=100, blank=True)
    integrante6 = models.CharField(max_length=100, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=[("pendente", "Pendente"), ("aceita", "Aceita"), ("rejeitada", "Recusada")],
        default="pendente",
    )

    def mover_para_equipe(self):
        equipe = Equipe.objects.create(
            nome=self.nome,
            integrante1=self.integrante1,
            integrante2=self.integrante2,
            integrante3=self.integrante3,
            integrante4=self.integrante4,
            integrante5=self.integrante5,
            integrante6=self.integrante6,
            data=self.data,
        )
        return equipe

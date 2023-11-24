from django.db import models
from django import forms


class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    integrante1 = models.CharField(max_length=100, blank=True)
    integrante2 = models.CharField(max_length=100, blank=True)
    integrante3 = models.CharField(max_length=100, blank=True)
    integrante4 = models.CharField(max_length=100, blank=True)
    integrante5 = models.CharField(max_length=100, blank=True)
    integrante6 = models.CharField(max_length=100, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    



    def __str__(self):
        return f"{self.nome}"

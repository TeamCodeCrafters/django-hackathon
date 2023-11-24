from django.db import models
from .equipe import Equipe

class Avaliacao(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipe} - {self.nota} - {self.comentario}"

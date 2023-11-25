from django.db import models
from .equipe import Equipe

class Avaliacao(models.Model):
    equipe = models.ForeignKey(Equipe, on_delete=models.RESTRICT, default=1)
    notaLayout = models.IntegerField()
    notaFuncionalidade = models.IntegerField()
    notaApresentacao = models.IntegerField()
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipe} - {self.comentario}"

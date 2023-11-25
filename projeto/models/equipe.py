from django.db import models

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    integrante1 = models.CharField(max_length=100, blank=True)
    integrante2 = models.CharField(max_length=100, blank=True)
    integrante3 = models.CharField(max_length=100, blank=True)
    integrante4 = models.CharField(max_length=100, blank=True)
    integrante5 = models.CharField(max_length=100, blank=True)
    integrante6 = models.CharField(max_length=100, blank=True)
    edicao = models.CharField(max_length=4, default=2023)
   

    @property
    def ano_criacao(self):
        return self.data.year
    
    def __str__(self):
        return f"{self.nome} - {self.ano_criacao}"


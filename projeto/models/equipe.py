from django.db import models
from core.models import User
class Equipe(models.Model):
        data = models.DateField(auto_now_add=True)
        user = models.ForeignKey(
        User,    
        on_delete=models.CASCADE,
        related_name="ordensservico",
        default=None,
        null=True,
    )
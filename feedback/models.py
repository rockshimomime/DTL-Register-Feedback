from django.db import models

# Create your models here.


class Registro(models.Model):
    nome = models.CharField(max_length=100)
    estilo = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    nota = models.DecimalField(max_digits=2, decimal_places=1)

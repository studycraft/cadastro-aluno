from django.db import models

from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    ra = models.CharField(max_length=8, unique=True)
    turma = models.CharField(max_length=50)
    trilhas = models.CharField(max_length=200)  # separadas por vírgula

    def __str__(self):
        return f"{self.nome} ({self.ra})"


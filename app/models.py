"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Curso(models.Model):
    nome = models.CharField(max_length=300)
    periodo = models.CharField(max_length=40)
    instituicao = models.CharField(max_length=300)

class Vestibular(models.Model):
    nome = models.CharField(max_length=200)


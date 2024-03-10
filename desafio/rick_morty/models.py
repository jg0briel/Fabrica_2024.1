from django.db import models

# Create your models here.

class RickMortyModel(models.Model):
    nome = models.CharField(verbose_name="Nome do personagem", max_length=40, blank =True, null=True)
    especie = models.CharField(verbose_name="Especie", max_length=40, blank=True, null=True)
    genero = models.CharField(verbose_name="Gênero", max_length=40, blank=True, null=True)
    origem = models.CharField(verbose_name="Local de origem", max_length=40, blank=True, null=True)
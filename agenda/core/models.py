from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=200, blank=True, null=True)

class Meta:
    db_table = 'evento'

def __str__(self):
    return self.titulo


def get_evento_atrasado(self):
    if self.data_evento < datetime.now():
        return True
    else:
        return False
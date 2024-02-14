from django.db import models

#importando modelos 
from django.contrib.auth.models import User

# Create your models here.
class ClaseModelo(models.Model):
  estado = models.BooleanField(default=True)
  fechaCreacion = models.DateTimeField(auto_now_add=True)
  fechaModificada = models.DateTimeField(auto_now=True)
  usuarioCreado = models.ForeignKey(User, on_delete=models.CASCADE)
  usuarioModificado = models.IntegerField(blank=True, null=True)

  class Meta:
    #permite no tener en cuenta las migraciones del modelo ClaseModelo
    abstract = True

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    imagen = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class VideoJuego(models.Model):
    titulo = models.CharField(max_length=255, blank=False, null=False)
    descripcion = models.TextField()
    annio = models.PositiveBigIntegerField()
    imagen = models.CharField(max_length=255, blank=True, null=True)
    plataforma = models.ForeignKey(
        Plataforma, on_delete=models.PROTECT, 
        related_name='videojuego'
    )
    genero = models.ForeignKey(
        Genero, on_delete=models.PROTECT, 
        related_name='videojuego'
    )

    def __str__(self):
        return f'{self.titulo} ({self.annio})'
    
class UserProfile(models.Model):
    # A continuación, ejemplos de algunos campos que se quieren asociar al usuario
    rut = models.CharField(max_length=12, unique=True, blank=False, null=False)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=12, unique=True, blank=False, null=False)
    vip = models.BooleanField(default=False)
    
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        id = self.user.id
        nombre = self.user.first_name
        apellido = self.user.last_name
        usuario = self.user.username
        rut = self.rut

        return f'{id} - {nombre} {apellido} - ({usuario}) - RUT: {rut}'


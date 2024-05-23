from django.db import models
# Create your models here.
from django.db import models
from django.shortcuts import render


# Create your models here.

class Usuario(models.Model):
    ROLES = (
        (1, "admin"),
        (3, "docente")
    )
    nombre_apellido = models.CharField(max_length=30)
    tipo_documento = models.CharField(max_length=30)
    numero_documento = models.CharField(max_length=30, default=0)
    telefono = models.IntegerField(default=0)
    correo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(default=0)
    contrasena = models.CharField(max_length=30)
    rol = models.IntegerField(choices=ROLES)

    def __str__(self):
        return f"{self.nombre_apellido}"



class Mensaje(models.Model):
    descripcion = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion[:50]  # Devuelve los primeros 50 caracteres de la descripción como representación del objeto

from django.db import models
from django.contrib.auth.models import AbstractUser

class Auto(models.Model):
    id = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=50, verbose_name="Marca")
    Modelo = models.CharField(max_length=50, verbose_name="Modelo")
    Anio = models.CharField(max_length=4,verbose_name="Año")
    Placa = models.CharField(max_length=7,verbose_name="Placa")
    Disponibilidad = models.BooleanField(default=False)
    
    
    def __str__(self):
        fila = "Marca: " + self.Marca + " - " + "Modelo: " + self.Modelo
        return fila
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('Nombre de usuario', max_length=30, unique=True)
    password= models.CharField('Contraseña', max_length=30)
    Nombres = models.CharField('Nombres completos', max_length=100)
    Apellidos= models.CharField(max_length=100)
    DNI= models.CharField(max_length=8, unique=True)
    Email= models.CharField(max_length=100, unique=True)
    Telefono= models.CharField(max_length=11)
    FechaNacimiento= models.DateField('Fecha de nacimiento')
    Direccion= models.CharField('Dirección', max_length=100)
    NroLicencia= models.CharField('Número de licencia', max_length=12, unique=True)
    FechaExpLicencia= models.DateField('Fecha de exp. de licencia')

    
    def __str__(self):
        fila = "Nombres: " + self.Nombres + " - " + "Apellido: " + self.Apellidos
        return fila

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    User = models.CharField(max_length=100, verbose_name="User")
    Contrasena = models.CharField(max_length=30, verbose_name="Contraseña")
    NombresApellidos = models.CharField(max_length=100, verbose_name="Nombres y Apellidos")
    Cargo= models.CharField(max_length=30, verbose_name="Cargo")
    Email= models.CharField(max_length=100, verbose_name="Email")
    Telefono= models.CharField(max_length=11, verbose_name="Teléfono")
    
    def __str__(self):
        fila = "Cargo: " + self.Cargo + " - " + "Nombres: " + self.NombresApellidos
        return fila


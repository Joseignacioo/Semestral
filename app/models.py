from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Marca")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=70)
    imagen = models.ImageField(upload_to="productos",null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0, verbose_name="Stock")
    
    def __str__(self):
        return self.nombre
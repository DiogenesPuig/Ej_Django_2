from django.db import models

# Create your models here.
class Direccion(models.Model):
    Calle = models.CharField(max_length=50)
    Numero = models.IntegerField()
    Comuna = models.CharField(max_length=50)
    Ciudad = models.CharField(max_length=50)

class Proveedor(models.Model):
    Provedor_Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    WEB = models.CharField(max_length=50) #UrlField() probar usar (???)
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

class Categoria(models.Model):
    Categoria_Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=100)

class Producto(models.Model):
    Producto_Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Precio = models.IntegerField()
    Stock = models.IntegerField()

class Detalle(models.Model):
    Cantidad  = models.IntegerField()

class Venta(models.Model):
    Venta_Id = models.AutoField(primary_key=True)
    Fecha = models.DateField()
    Monto_Final = models.IntegerField()
    Descuento = models.IntegerField()

class Cliente(models.Model):
    Cliente_Id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=20) #Hay que cambiarlo para que guarde mas de 1 telefono
    Direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

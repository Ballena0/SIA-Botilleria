from django.db import models
from datetime import datetime

# Create your models here.

class FORMATO(models.Model):
    FORMATO_ID = models.AutoField(primary_key=True)
    UNIDADES = models.CharField(max_length=50)
    DESCRIPCION_FOR = models.CharField(max_length=50)

    def __str__(self):
        return self.UNIDADES+' '+self.DESCRIPCION_FOR

class PRODUCTO(models.Model):
    FORMAT_PROD = models.ForeignKey(FORMATO, on_delete=models.CASCADE)
    ID_PROD = models.AutoField(primary_key=True)
    NOMBRE_PROD = models.CharField(max_length=50)
    PRECIO = models.IntegerField(default=0)
    STOCK = models.IntegerField(default=0)

    def __str__(self):
        return self.NOMBRE_PROD+' '+self.FORMAT_PROD.UNIDADES+' '+self.FORMAT_PROD.DESCRIPCION_FOR

class PROVEEDOR(models.Model):
    RUT = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=50)
    TELEFONO = models.IntegerField(default=0)

    def __str__(self):
        return (self.NOMBRE)

class Pedido(models.Model):
    PEDIDO_ID = models.AutoField(primary_key=True)
    PROVEEDOR = models.ForeignKey(PROVEEDOR, on_delete=models.CASCADE)
    FECHA = models.DateTimeField(default=datetime.now, blank=True)
    INGRESADO_POR = models.CharField(max_length=50)

    def __str__(self):
        return "N°"+str(self.PEDIDO_ID)+' '+str(self.FECHA)

class IngresoProducto(models.Model):
    IP_ID = models.AutoField(primary_key=True)
    NUMPEDIDO = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    PRODUCTO = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    CANTIDAD = models.IntegerField(default=1)
    DESCRIPCION = models.CharField(max_length=100)

    def stockp(self):
        if PRODUCTO.ID_PROD == self.PRODUCTO.ID_PROD:
            self.PRODUCTO.STOCK = self.CANTIDAD
        self.save()

    def __str__(self):
        return self.PRODUCTO.NOMBRE_PROD+'; '+self.DESCRIPCION


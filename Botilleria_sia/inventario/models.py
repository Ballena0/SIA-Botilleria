from django.db import models

# Create your models here.

class  FORMATO(models.Model):
    CODIGO_F = models.IntegerField(primary_key=True)
    CANTIDAD = models.IntegerField()
    CANT_P = models.IntegerField()
    TIPO_FORMATO = models.CharField(max_length=50)
    DESCRIPTCION_FOR = models.CharField(max_length=50)

class PRODUCTO(models.Model):
    ID_PROD = models.IntegerField(primary_key=True)
    NOMBRE_PROD = models.CharField(max_length=50)
    FORM_PROD = models.ForeignKey(FORMATO, on_delete=models.CASCADE)
    PRECIO = models.IntegerField()
    STOCK = models.IntegerField()
    DESCRIPCION_PROD = models.CharField(max_length=50)

class PROVEEDOR(models.Model):
    RUT_PROV = models.IntegerField(primary_key=True)
    NOMBRE_PROV = models.CharField(max_length=50)
    TELEFONO_PROV = models.IntegerField()
    DESCRIPCION_PROV = models.CharField(max_length=50)

class REGISTRO_BOD(models.Model):
    COD_REG_BOD = models.IntegerField(primary_key=True)
    ID_PRODUCT = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    COD_PROV = models.ForeignKey(PROVEEDOR, on_delete=models.CASCADE)
    DESCRIPCION_REG = models.CharField(max_length=50)

class VENDEDOR(models.Model):
    RUT_V = models.IntegerField(primary_key=True)
    NOMBRE_V = models.CharField(max_length=50)
    CARGO = models.CharField(max_length=50)

class VENTA(models.Model):
    CODIGO_V = models.IntegerField(primary_key=True)
    NUM_VENTA = models.IntegerField()
    PRODUCTO_V = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    CANTIDAD = models.IntegerField()




##texto whitten-sia

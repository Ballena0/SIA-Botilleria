from django.db import models
from datetime import datetime
from inventario.models import PRODUCTO

# Create your models here.

class TIPO_PAGO(models.Model):
    PAGO_ID = models.IntegerField(primary_key=True)
    TIPO_PAGO = models.CharField(max_length=50)

    def __str__(self):
        return (self.TIPO_PAGO)

class VENTA(models.Model):
    VENTA_ID = models.AutoField(primary_key=True)
    FECHA = models.DateTimeField(default=datetime.now, blank=True)
    TIPO_PAGO = models.ForeignKey(TIPO_PAGO, on_delete=models.CASCADE)
    TOTAL_A_PAGAR = models.IntegerField(default=0)

    def __str__(self):
        return "N°"+str(self.VENTA_ID)+' '+str(self.FECHA)

class DETALLE(models.Model):
    NUMERO_DE_VENTA = models.ForeignKey(VENTA, on_delete=models.CASCADE)
    DETALLE_ID = models.AutoField(primary_key=True)
    PRODUCTO = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    CANTIDAD = models.IntegerField(default=0)

    def __str__(self):
        return (self.PRODUCTO.NOMBRE_PROD+" "+self.PRODUCTO.FORMAT_PROD.UNIDADES+" "+self.PRODUCTO.FORMAT_PROD.DESCRIPCION_FOR+" x "+str(self.CANTIDAD))

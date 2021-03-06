from django.db import models
from datetime import date, datetime
from inventario.models import PRODUCTO

class TipoPago(models.Model):
    PAGO_ID = models.IntegerField(primary_key=True)
    TIPO_PAGO = models.CharField(max_length=50)

    def __str__(self):
        return (self.TIPO_PAGO)

class VENTA(models.Model):
    VENTA_ID = models.AutoField(primary_key=True)
    FECHA = models.DateField(default=date.today(), blank=True)
    HORA = models.TimeField(default=datetime.now().time(), blank=True)
    TIPO_PAGO = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    VENDEDOR = models.CharField(max_length=50)
    TOTAL_A_PAGAR = models.IntegerField(default=0)
    ESTADO = models.BooleanField(default=False)

    def totalv(self):
        self.TOTAL_A_PAGAR = sum(DETALLE.objects.values_list('TOTAL_DETALLE', flat=True).filter(NUMERO_DE_VENTA=self.VENTA_ID))
        self.save()

    def estado(self):
        self.ESTADO = True
        self.save()

    def __str__(self):
        return 'N° '+str(self.VENTA_ID)+' '+str(self.FECHA)+' '+str(self.HORA)

class DETALLE(models.Model):
    NUMERO_DE_VENTA = models.ForeignKey(VENTA, on_delete=models.CASCADE)
    DETALLE_ID = models.AutoField(primary_key=True)
    PRODUCTO = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE)
    CANTIDAD = models.IntegerField(default=1)
    TOTAL_DETALLE = models.IntegerField(default=0)
    ESTADO = models.BooleanField(default=False)

    def totald(self):
        self.TOTAL_DETALLE = self.CANTIDAD*self.PRODUCTO.PRECIO
        self.save()

    def stockd(self):
        producto = self.PRODUCTO
        producto.STOCK = producto.STOCK - self.CANTIDAD
        producto.save()

    def __str__(self):
        return (self.PRODUCTO.NOMBRE_PROD+" "+self.PRODUCTO.FORMAT_PROD.UNIDADES+" "+self.PRODUCTO.FORMAT_PROD.DESCRIPCION_FOR+" x "+str(self.CANTIDAD))

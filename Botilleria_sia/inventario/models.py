from django.db import models

# Create your models here.

class FORMATO(models.Model):
    FORMATO_ID = models.IntegerField(primary_key=True)
    CANTIDAD = models.IntegerField(default=0)
    CANT_P = models.IntegerField(default=0)
    TIPO_FORMATO = models.CharField(max_length=50)
    DESCRIPCION_FOR = models.CharField(max_length=50)

    def __str__(self):
        return self.TIPO_FORMATO

class PRODUCTO(models.Model):
    FORM_PROD = models.ForeignKey(FORMATO, on_delete=models.CASCADE)
    ID_PROD = models.IntegerField(primary_key=True)
    NOMBRE_PROD = models.CharField(max_length=50)
    PRECIO = models.IntegerField(default=0)
    STOCK = models.IntegerField(default=0)
    DESCRIPCION_PROD = models.CharField(max_length=50)

    def __str__(self):
        return self.NOMBRE_PROD






##texto whitten-sia

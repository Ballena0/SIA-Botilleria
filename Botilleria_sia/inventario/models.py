from django.db import models

# Create your models here.

class FORMATO(models.Model):
    FORMATO_ID = models.IntegerField(primary_key=True)
    UNIDADES = models.CharField(max_length=50)
    DESCRIPCION_FOR = models.CharField(max_length=50)

    def __str__(self):
        return (self.UNIDADES+" "+self.DESCRIPCION_FOR)

class PRODUCTO(models.Model):
    FORM_PROD = models.ForeignKey(FORMATO, on_delete=models.CASCADE)
    ID_PROD = models.IntegerField(primary_key=True)
    NOMBRE_PROD = models.CharField(max_length=50)
    PRECIO = models.IntegerField(default=0)
    STOCK = models.IntegerField(default=0)

    def __str__(self):
        return (self.NOMBRE_PROD+" "+self.FORM_PROD.UNIDADES+" "+self.FORM_PROD.DESCRIPCION_FOR)
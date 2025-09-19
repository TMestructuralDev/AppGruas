from django.db import models

# Create your models here.
class Note (models.Model):
    
    nombre = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    empresa = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    equipo = models.CharField(max_length=50, blank=True, null=True)
    operador = models.CharField(max_length=20, blank=True, null=True)
    ayudante = models.CharField(max_length=20, blank=True, null=True)
    trabajo_realizar = models.TextField(max_length=100)
    
    # Tiempos
    salida = models.TimeField()
    llegada = models.TimeField()
    termino = models.TimeField()
    retorno = models.TimeField()

    # Costos
    costo_hr_maniobra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Firma cliente (puede ser imagen en base64 o archivo)
    firma_cliente = models.ImageField(upload_to="firmas/")

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    # Estado de la nota (por defecto abierta)
    nota_abierta = models.BooleanField(default=True)

    def __str__(self):
        return f"Nota de {self.nombre} - {self.fecha}"
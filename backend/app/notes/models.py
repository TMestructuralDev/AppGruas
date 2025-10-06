from django.db import models

# Create your models here.
class Note (models.Model):
    
    nombre = models.CharField(max_length=20, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    empresa = models.CharField(max_length=20, blank=True, null=True)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=50, blank=True, null=True)
    equipo = models.CharField(max_length=20, blank=True, null=True)
    operador = models.CharField(max_length=20, blank=True, null=True)
    ayudante = models.CharField(max_length=20, blank=True, null=True)
    trabajo_realizar = models.CharField(max_length=100, blank=True, null=True)
    
    # Tiempos
    salida = models.TimeField(blank=True, null=True)
    llegada = models.TimeField(blank=True, null=True)
    termino = models.TimeField(blank=True, null=True)
    retorno = models.TimeField(blank=True, null=True)
    total_horas = models.FloatField(blank=True, null=True)

    # Costos
    costo_hora = models.FloatField(blank=True, null=True)
    costo_total = models.FloatField(blank=True, null=True)
    costo_total_iva = models.FloatField(blank=True, null=True)

    # Firma cliente 
    firma_cliente = models.CharField(max_length=20, blank=True, null=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    # Estado de la nota (por defecto abierta)
    nota_abierta = models.BooleanField(default=True)

    def __str__(self):
        return f"Nota de {self.nombre} - {self.fecha}"
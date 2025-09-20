from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "id", "nombre", "telefono", "empresa", "fecha", "ubicacion", "equipo", "operador",
        "ayudante", "trabajo_realizar",
         "salida", "llegada", "termino", "retorno","total_horas",
         "costo_hora", "costo_total", "costo_total_iva", 
         "firma_cliente", "creado_en", "actualizado_en","nota_abierta",
    )
    list_filter = ("nota_abierta", "fecha", "empresa")
    search_fields = ("nombre", "empresa", "ubicacion", "operador", "ayudante")
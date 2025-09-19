from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "id", "nombre", "telefono", "empresa", "fecha", "ubicacion", "equipo", "operador",
        "ayudante", "trabajo_realizar",
         "salida", "llegada", "termino", "retorno",
         "costo_hr_maniobra", "firma_cliente", "creado_en", "actualizado_en","nota_abierta",
    )
    list_filter = ("nota_abierta", "fecha", "empresa")
    search_fields = ("nombre", "empresa", "ubicacion", "operador", "ayudante")
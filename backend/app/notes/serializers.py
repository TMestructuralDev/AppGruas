from rest_framework import serializers
from .models import Note
from datetime import datetime, timedelta

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"

    def validate(self, data):
        salida = data.get("salida")
        llegada = data.get("llegada")
        termino = data.get("termino")
        retorno = data.get("retorno")
        costo_hora = data.get("costo_hora") or 0

        # Hours
        if salida and retorno:
            delta = datetime.combine(data["fecha"], retorno) - datetime.combine(data["fecha"], salida)
            horas = delta.total_seconds() / 3600
            data["total_horas"] = round(horas, 2)
        else:
            data["total_horas"] = 0

        # Costs
        data["costo_total"] = round(data["total_horas"] * costo_hora, 2)
        data["costo_total_iva"] = round(data["costo_total"] * 1.16, 2)  # IVA 16%

        return data
    

class NoteOpenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "nombre", "fecha", "operador", "nota_abierta"]
        read_only_fields = ["id", "nota_abierta"]

    def create(self, validated_data):
        validated_data.setdefault("nota_abierta", True)
        return super().create(validated_data)
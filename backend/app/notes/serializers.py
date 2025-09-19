from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        extra_kwargs = {
            "nombre": {"required": True},
            "telefono": {"required": True},
            "fecha": {"required": True},
            "salida": {"required": True},
            "llegada": {"required": True},
            "termino": {"required": True},
            "retorno": {"required": True},
            "trabajo_realizar": {"required": True},
            "firma_cliente": {"required": True},
        }
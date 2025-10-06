from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__" 
        
    
    
class NoteOpenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "nombre", "fecha", "operador", "nota_abierta"]
        read_only_fields = ["id", "nota_abierta"]

    def create(self, validated_data):
        validated_data.setdefault("nota_abierta", True)
        return super().create(validated_data)
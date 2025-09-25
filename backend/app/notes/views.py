from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Note
from .serializers import NoteSerializer, NoteOpenSerializer
from rest_framework.response import Response
from rest_framework import status

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    

class OpenNoteAPIView(APIView):
    def post(self, request, *args, **kwargs):
        print("DATA RECEIVED:", request.data)  # <--- agrega esto temporalmente
        serializer = NoteOpenSerializer(data=request.data)
        if serializer.is_valid():
            note = serializer.save()
            return Response(NoteOpenSerializer(note).data, status=status.HTTP_201_CREATED)
        print("ERRORS:", serializer.errors)  # <--- imprime errores
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
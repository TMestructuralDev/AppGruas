
class NoteAdapter:
    @staticmethod
    def to_card_format(note):
        """
        Convierte un diccionario de nota del backend al formato que espera OpenNoteCard.
        """
        return {
            "nombre": note.get("nombre", "Sin nombre"),
            "operador": note.get("operador", "Sin operador"),
            "ayudante": note.get("ayudante", "Sin ayudante"),
            "empresa": note.get("empresa", "Sin empresa"),
            "ubicacion": note.get("ubicacion", "Sin ubicación"),
            "llegada": note.get("llegada", "Sin hora"),
            "fecha": note.get("fecha", "Sin fecha"),
            "equipo": note.get("equipo", "Sin equipo"),
        }

    @staticmethod
    def to_card_list(notes):
        """
        Convierte una lista de notas en formato backend a lista de notas para OpenNoteCard.
        """
        return [NoteAdapter.to_card_format(note) for note in notes]
    
    
    @staticmethod
    def to_closed_card_list(notes):
        """Versión semántica para notas cerradas (usa el mismo formato que las abiertas)."""
        return [NoteAdapter.to_card_format(note) for note in notes]
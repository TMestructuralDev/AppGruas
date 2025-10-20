
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
    def to_form_format(note):
        """Convierte un diccionario completo del backend al formato que espera el formulario."""
        return {
        "id": note.get("id"),
        "nombre": note.get("nombre"),
        "telefono": note.get("telefono"),
        "empresa": note.get("empresa"),
        "fecha": note.get("fecha"),
        "ubicacion": note.get("ubicacion"),
        "equipo": note.get("equipo"),
        "operador": note.get("operador"),
        "ayudante": note.get("ayudante"),
        "trabajo_a_realizar": note.get("trabajo_realizar"),  
        "salida": note.get("salida"),
        "llegada": note.get("llegada"),
        "termino": note.get("termino"),
        "retorno": note.get("retorno"),
        "horas_de_trabajo": note.get("total_horas"),          
        "costo_hr_o_maniobra": note.get("costo_hora"),       
        "costo_total": note.get("costo_total"),
        "costo_total_con_iva": note.get("costo_total_iva"),
        "firma": note.get("firma_cliente"),                  
    }

    @staticmethod
    def to_card_list(notes):
        """
        Convierte una lista de notas en formato backend a lista de notas para OpenNoteCard.
        """
        return [NoteAdapter.to_form_format(note) for note in notes]
    
    
    @staticmethod
    def to_closed_card_list(notes):
        """Versión semántica para notas cerradas (usa el mismo formato que las abiertas)."""
        return [NoteAdapter.to_form_format(note) for note in notes]
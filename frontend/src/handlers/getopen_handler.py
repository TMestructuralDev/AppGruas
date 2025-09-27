from core.usecases.getopen_notes import get_open_notes

def handle_open_notes():
    """
    Handler para la vista de notas abiertas.
    Llama al usecase y devuelve la lista de notas adaptadas.
    """
    try:
        notes = get_open_notes()
        return notes
    except Exception as e:
        print("Error en handle_open_notes:", e)
        return []
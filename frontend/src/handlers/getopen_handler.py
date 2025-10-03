from core.usecases.getopen_notes import get_open_notes
from core.errors.app_exceptions import NotesFetchError
from handlers.snackbar_handler import show_snack
import flet as ft

def handle_open_notes(page: ft.Page):
    """
    Handler para la vista de notas abiertas.
    Llama al usecase y devuelve la lista de notas adaptadas.
    """
    try:
        notes = get_open_notes()
        if not notes:
            show_snack(page, "No hay notas abiertas disponibles.", success=False)
        return notes
    except NotesFetchError as e:
        show_snack(page, e.args[0], success=False)
        return []
    except Exception as e:
        show_snack(page, "Error inesperado al cargar notas abiertas", success=False)
        return []
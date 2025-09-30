from utils.extract_data import extract_data, extract_open_note_data
from core.usecases.send_note import send_note
from core.usecases.open_note import open_note
import threading
from handlers.snackbar_handler import show_snack
import flet as ft

def handle_send_note(form_column):
    """
    Handler:
    1. Extract form data
    2. Call Core
    """
    form_data = extract_data(form_column)
    send_note(form_data)
    

def handle_open_note(form_column, page: ft.Page):
    """
    Ejecuta open_note en un hilo para no bloquear la UI de Flet.
    Muestra SnackBar de éxito/error.
    """
    form_data = extract_open_note_data(form_column)

    def task():
        try:
            # Ejecuta la lógica de abrir la nota
            open_note(form_data)
            # Muestra SnackBar de éxito
            show_snack(page, "Nota abierta con éxito!", success=True)
        except Exception as err:
            print(f"Error al abrir nota: {err}")
            # Muestra SnackBar de error
            show_snack(page, "Error al abrir la nota", success=False)

    threading.Thread(target=task).start()
from utils.extract_data import extract_data, extract_open_note_data
from core.usecases.create_note import create_note
from core.usecases.open_note import open_note
import threading
import flet as ft

def handle_note(form_column):
    """
    Handler:
    1. Extract form data
    2. Call Core
    """
    form_data = extract_data(form_column)
    create_note(form_data)
    

def handle_open_note(form_column, page: ft.Page):
    """
    Ejecuta open_note en un hilo para no bloquear la UI de Flet.
    Muestra SnackBar de éxito/error.
    """
    form_data = extract_open_note_data(form_column)

    
    def task():
        try:
            open_note(form_data)
            # Nota abierta correctamente, no mostramos mensaje
        except Exception as err:
            print(f"Error al abrir nota: {err}")  # opcional para debug

    threading.Thread(target=task).start()
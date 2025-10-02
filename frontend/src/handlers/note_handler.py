from utils.extract_data import extract_data, extract_open_note_data
from core.usecases.send_note import send_note
from core.usecases.open_note import open_note
from core.errors.app_exceptions import ValidationError, GatewayError
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
    

def handler_open_note(form_column, page: ft.Page):
    """
    Ejecuta open_note en un hilo.
    Maneja errores de validación y gateway con SnackBars.
    """
    form_data = extract_open_note_data(form_column)

    def task():
        try:
            open_note(form_data)
            show_snack(page, "Nota abierta con éxito!", success=True)
        except ValidationError as ve:
            show_snack(page, f"Validación: {ve.message}", success=False)
        except GatewayError as ge:
            show_snack(page, f"Backend: {ge.message}", success=False)
        except Exception as err:
            print(f"Error inesperado: {err}")
            show_snack(page, "Error inesperado al abrir la nota", success=False)

    threading.Thread(target=task).start()
from utils.extract_data import extract_note_data, extract_open_note_data
from core.usecases.send_note import send_note
from core.usecases.open_note import open_note
from core.usecases.get_closed_notes import get_closed_notes
from core.errors.app_exceptions import ValidationError, GatewayError
import threading
from handlers.snackbar_handler import show_snack
import flet as ft

def handler_send_note(form_column, page: ft.Page):
    """
    Handler:
    1. Extract form data
    2. Call Core
    """
    page.update() # Probar sin esta funcion
    form_data = extract_note_data(form_column)

    def task():
        try:
            send_note(form_data)
            show_snack(page, "Nota enviada con éxito!", success=True)
        except ValidationError as ve:
            show_snack(page, f"Validación: {ve.message}", success=False)
        except GatewayError as ge:
            show_snack(page, f"Backend: {ge.message}", success=False)
        except Exception as err:
            print(f"Error inesperado: {err}")
            show_snack(page, "Error inesperado al enviar la nota", success=False)

    threading.Thread(target=task).start()
    
    

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

    
    
def handler_closed_notes(page: ft.Page):
    """
    Handler para obtener las notas cerradas.
    Llama al caso de uso en el core y devuelve la lista de notas.
    """
    notes_result = []

    def task():
        nonlocal notes_result
        try:
            notes = get_closed_notes()
            
            notes_result = notes
        except GatewayError as ge:
            show_snack(page, f"Error de backend: {ge.message}", success=False)
        except Exception as err:
            
            show_snack(page, "Error inesperado al obtener notas cerradas", success=False)

    thread = threading.Thread(target=task)
    thread.start()
    thread.join()  # Esperamos a que termine para devolver los datos
    return notes_result
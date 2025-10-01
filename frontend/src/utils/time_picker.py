import flet as ft
import datetime

def time_picker_button(page: ft.Page, textfield: ft.TextField, label="Hora"):
    """
    Botón que abre un TimePicker y actualiza el TextField correspondiente
    con el valor en formato HH:MM listo para enviar al backend.
    """
    def open_picker(e):
        tp = ft.TimePicker(
            confirm_text="Confirmar",
            help_text="Selecciona la hora",
            on_change=on_change,
        )
        page.open(tp)

    def on_change(e):
        hora = e.control.value
        if hora:
            # Guardamos directamente en HH:MM
            if isinstance(hora, datetime.datetime):
                textfield.value = hora.strftime("%H:%M")
            else:
                textfield.value = str(hora)  # en caso que sea datetime.time
            textfield.update()
            print(f"{textfield.label} seleccionada:", textfield.value)

    button = ft.ElevatedButton(
        label,
        icon=ft.Icons.ACCESS_TIME,
        on_click=open_picker
    )
    return button
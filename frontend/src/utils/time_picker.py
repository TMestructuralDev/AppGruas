import flet as ft
import datetime

def time_picker_field(page: ft.Page, label: str = "Hora"):
    """
    Returns a Row with:
    - ElevatedButton to open the TimePicker
    - Text showing the selected time
    Stores the selected time as datetime.time in row.value
    """
    selected_time_text = ft.Text("")
    row = ft.Row(
        controls=[],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    # Inicializamos el valor de la hora
    row.value = None

    def handle_change(e):
        if e.control.value:
            # e.control.value puede ser datetime.datetime, convertimos a datetime.time
            if isinstance(e.control.value, datetime.datetime):
                row.value = e.control.value.time()
            else:
                row.value = e.control.value

            selected_time_text.value = row.value.strftime("%H:%M")
            selected_time_text.update()
            print("Nueva hora seleccionada:", row.value)
            print("Tipo de dato:", type(row.value))

    def handle_dismiss(e):
        pass  

    def open_picker(e):
        page.open(
            ft.TimePicker(
                confirm_text="Confirmar",
                help_text="Selecciona la hora",
                on_change=handle_change,
                on_dismiss=handle_dismiss,
            )
        )

    button = ft.ElevatedButton(
        label,
        icon=ft.Icons.ACCESS_TIME,
        on_click=open_picker
    )

    row.controls.extend([button, selected_time_text])
    return row

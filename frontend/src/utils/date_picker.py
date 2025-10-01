import datetime
import flet as ft

def date_picker_button(page: ft.Page, textfield: ft.TextField):
    """
    Solo crea un botón que abre el DatePicker.
    Cuando se selecciona la fecha, se guarda en el TextField proporcionado.
    """
    def open_picker(e):
        dp = ft.DatePicker(
            first_date=datetime.date(2025,1,1),
            last_date=datetime.date(2050,12,31),
            on_change=on_change,
        )
        page.open(dp)

    def on_change(e):
        fecha = e.control.value
        if fecha:
            # Solo fecha en formato YYYY-MM-DD
            textfield.value = fecha.strftime("%Y-%m-%d")
            textfield.update()
            print("Fecha seleccionada:", textfield.value)

    button = ft.ElevatedButton("Seleccionar Fecha", on_click=open_picker)
    return button
import datetime
import flet as ft

def date_picker_field(page: ft.Page, label: str = "Fecha"):
    """
    Returns a Row with a button and text.
    Stores the selected date as a datetime.date in row.value.
    """
    selected_date_text = ft.Text("")
    row = ft.Row(
        controls=[],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    # Inicializamos el valor de la fecha
    row.value = None

    def handle_change(e):
        if e.control.value:
            # e.control.value puede ser datetime.datetime
            # Convertimos a datetime.date
            if isinstance(e.control.value, datetime.datetime):
                row.value = e.control.value.date()
            else:
                row.value = e.control.value

            selected_date_text.value = row.value.strftime("%d/%m/%Y")
            selected_date_text.update()
            print("Nueva fecha seleccionada:", row.value)
            print("Tipo de dato:", type(row.value))

    def handle_dismiss(e):
        pass

    def open_picker(e):
        page.open(
            ft.DatePicker(
                first_date=datetime.date(year=2025, month=1, day=1),
                last_date=datetime.date(year=2050, month=12, day=31),
                on_change=handle_change,
                on_dismiss=handle_dismiss,
            )
        )

    button = ft.ElevatedButton(
        label,
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=open_picker
    )

    row.controls.extend([button, selected_date_text])
    return row

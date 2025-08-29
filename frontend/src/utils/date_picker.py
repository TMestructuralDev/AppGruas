import datetime
import flet as ft


def date_picker_field(page: ft.Page, label: str = "Fecha"):
    """
    Retorna un TextField y configura un DatePicker que se abre al dar click.
    La fecha seleccionada se muestra en el TextField.
    """
    
    selected_date_text = ft.Text("")

    def handle_change(e):
        if e.control.value:
            selected_date_text.value = e.control.value.strftime("%d/%m/%Y")
            selected_date_text.update()

    def handle_dismiss(e):
        pass

    def open_picker(e):
        page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=2025, month=1, day=1),
                last_date=datetime.datetime(year=2050, month=12, day=31),
                on_change=handle_change,
                on_dismiss=handle_dismiss,
            )
        )


    button = ft.ElevatedButton(
        label,
        icon=ft.Icons.CALENDAR_MONTH,
        on_click=open_picker
    )
    
    return ft.Row(
        controls=[button, selected_date_text],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

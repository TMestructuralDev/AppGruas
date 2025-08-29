import flet as ft

def time_picker_field(page: ft.Page, label: str = "Hora"):
    """
    Retorna un Row con:
    - ElevatedButton que abre el TimePicker
    - Text que muestra la hora seleccionada
    """
    selected_time_text = ft.Text("")


    def handle_change(e):
        if e.control.value:
            selected_time_text.value = e.control.value.strftime("%H:%M")
            selected_time_text.update()

    
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

    
    return ft.Row(
        controls=[button, selected_time_text],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )
import flet as ft
from utils.date_picker import date_picker_field
from utils.time_picker import time_picker_field
from components.signature import create_signature_canvas, clear_canvas

class NoteForm(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.spacing = 10
        self.expand = True
                # ---------- BOTÓN REGRESAR FIJO ARRIBA ----------
        self.back_button = ft.TextButton(
            text="Regresar",
            icon=ft.Icons.ARROW_BACK,
            icon_color=ft.Colors.GREEN_400,
            on_click=lambda e: page.on_view_pop(page.views)
        )

        # ---------- FORMULARIO SCROLL ----------
        self.form = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=10,
            controls=[
                ft.TextField(label="Nombre", hint_text="Nombre"),
                ft.TextField(label="Telefono", hint_text="Telefono"),
                ft.TextField(label="Empresa", hint_text="Empresa"),
                date_picker_field(page, label="Fecha"),
                ft.TextField(label="Ubicacion", hint_text="Ubicacion"),
                ft.TextField(label="Equipo", hint_text="Equipo"),
                ft.TextField(label="Operador", hint_text="Operador"),
                ft.TextField(label="Ayudante", hint_text="Ayudante"),
                ft.TextField(label="Trabajo a Realizar", hint_text="Trabajo a Realizar", multiline=True),
                time_picker_field(page, label="Salida"),
                time_picker_field(page, label="Llegada"),
                time_picker_field(page, label="Termino"),
                time_picker_field(page, label="Retorno"),
                ft.TextField(label="Costo Hr/Maniobra", hint_text="Costo Hr/Maniobra"),
                ft.Text("Firma Cliente:"),
                create_signature_canvas(width=150, height=150),
                ft.ElevatedButton("Limpiar Firma", on_click=lambda e: clear_canvas(self.controls[-2])),
                ft.ElevatedButton("Enviar Nota"),
                ft.TextButton("Abrir Nota", icon=ft.Icons.NOTE_ADD_OUTLINED, icon_color=ft.Colors.GREEN_400)
            ]
        )
        
        self.controls.extend([
            self.back_button,  
            self.form    
        ])
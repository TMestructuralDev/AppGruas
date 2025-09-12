import flet as ft
from utils.date_picker import date_picker_field
from utils.time_picker import time_picker_field
from components.widgets.signature import create_signature_canvas, clear_canvas

class NoteForm(ft.Column):
    def __init__(self, page: ft.Page,  note: dict = None): # note: dict es para prueba, eliminar
        super().__init__()
        self.spacing = 10
        self.expand = True
        self.signature_canvas = create_signature_canvas(width=150, height=150)
        
        # ---------- DATOS PRUEBA ----------
        # Extraemos valores si hay nota
        nombre = note.get("nombre", "") if note else ""
        telefono = note.get("telefono", "") if note else ""
        empresa = note.get("empresa", "") if note else ""
        ubicacion = note.get("ubicacion", "") if note else ""

        # ---------- FORM SCROLL ----------
        self.form = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=10,
            controls=[
                ft.TextField(value=nombre, label="Nombre", hint_text="Nombre"),
                ft.TextField(value= telefono, label="Telefono", hint_text="Telefono"),
                ft.TextField(value=empresa, label="Empresa", hint_text="Empresa"),
                date_picker_field(page, label="Fecha"),
                ft.TextField(value=ubicacion, label="Ubicacion", hint_text="Ubicacion"),
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
                self.signature_canvas,
                ft.ElevatedButton("Limpiar Firma", on_click=lambda e: clear_canvas(self.signature_canvas)),
                ft.ElevatedButton("Enviar Nota"),
                ft.TextButton("Abrir Nota", icon=ft.Icons.NOTE_ADD_OUTLINED, icon_color=ft.Colors.GREEN_400)
            ]
        )
        
        self.controls.append(self.form)
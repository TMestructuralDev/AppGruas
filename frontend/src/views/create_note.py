import flet as ft
from utils.date_picker import date_picker_field
from utils.time_picker import time_picker_field
from components.signature import create_signature_canvas, clear_canvas

class Create(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.spacing = 10
        self.expand = True
        self.scroll = ft.ScrollMode.ALWAYS 
        
        self.controls.append(
            ft.TextField(label="Nombre", hint_text="Nombre")
        )
        self.controls.append(
            ft.TextField(label="Telefono", hint_text="Telefono")
        )
        self.controls.append(
            ft.TextField(label="Empresa", hint_text="Empresa")
        )
        self.controls.append(
            date_picker_field(page, label="Fecha")
        )
        self.controls.append(
            ft.TextField(label="Ubicacion", hint_text="Ubicacion")
        )
        self.controls.append(
            ft.TextField(label="Equipo", hint_text="Equipo")
        )
        self.controls.append(
            ft.TextField(label="Operador", hint_text="Operador")
        )
        self.controls.append(
            ft.TextField(label="Ayudante", hint_text="Ayudante")
        )
        self.controls.append(
            ft.TextField(label="Trabajo a Realizar", hint_text="Trabajo a Realizar", multiline=True)
        )
        self.controls.append(
            time_picker_field(page, label="Salida")
        )
        self.controls.append(
            time_picker_field(page, label="Llegada")
        )
        self.controls.append(
            time_picker_field(page, label="Termino")
        )
        self.controls.append(
            time_picker_field(page, label="Retorno")
        )
        self.controls.append(
            ft.TextField(label="Costo Hr/Maniobra", hint_text="Costo Hr/Maniobra")
        )
        
        self.signature_canvas = create_signature_canvas(width=150, height=150)
        self.controls.append(ft.Text("Firma Cliente:"))
        self.controls.append(self.signature_canvas)
        self.controls.append(
            ft.ElevatedButton("Limpiar Firma", on_click=lambda e: clear_canvas(self.signature_canvas))
        )
        
        self.controls.append(
            ft.ElevatedButton("Enviar Nota")
        )
        
        self.controls.append(
            ft.TextButton("Abrir Nota", icon=ft.Icons.NOTE_ADD_OUTLINED, icon_color=ft.Colors.GREEN_400)
        )
        
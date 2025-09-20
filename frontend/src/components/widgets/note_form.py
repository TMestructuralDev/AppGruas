import flet as ft
from utils.date_picker import date_picker_field
from utils.time_picker import time_picker_field
from components.widgets.signature import create_signature_canvas, clear_canvas
from handlers.note_handler import handle_note


class NoteForm(ft.Column):
    def __init__(self, page: ft.Page): 
        super().__init__()
        self.spacing = 10
        self.expand = True
        self.signature_canvas = create_signature_canvas(width=150, height=150)
        

        # ---------- FORM SCROLL ----------
        self.form = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=10,
            controls=[
                ft.TextField(label="Nombre", hint_text="Nombre", max_length=20),
                ft.TextField(label="Telefono", hint_text="Telefono", max_length=10),
                ft.TextField(label="Empresa", hint_text="Empresa", max_length=20),
                date_picker_field(page, label="Fecha"),
                ft.TextField(label="Ubicacion", hint_text="Ubicacion", max_length=50),
                ft.TextField(label="Equipo", hint_text="Equipo", max_length=20),
                ft.TextField(label="Operador", hint_text="Operador", max_length=20),
                ft.TextField(label="Ayudante", hint_text="Ayudante", max_length=20),
                ft.TextField(label="Trabajo a Realizar", hint_text="Trabajo a Realizar", multiline=True),
                
                time_picker_field(page, label="Salida"),
                time_picker_field(page, label="Llegada"),
                time_picker_field(page, label="Termino"),
                time_picker_field(page, label="Retorno"),
                ft.TextField(label="Horas de Trabajo", hint_text="Total de Horas", max_length=10),
                
                ft.TextField(label="Costo Hr/Maniobra", hint_text="Costo Hr/Maniobra", max_length=10),
                ft.TextField(label="Costo Total", hint_text="Total", max_length=10),
                ft.TextField(label="Costo Total con IVA", hint_text="Costo Total con IVA", max_length=10),
                
                ft.Text("Firma Cliente:"),
                ft.TextField(label="Firma", hint_text="Firma", max_length=20),
                #self.signature_canvas,
                
                #ft.ElevatedButton("Limpiar Firma", on_click=lambda e: clear_canvas(self.signature_canvas)),
                ft.ElevatedButton("Enviar Nota"),
                ft.ElevatedButton("Abrir Nota", icon=ft.Icons.NOTE_ADD_OUTLINED, icon_color=ft.Colors.GREEN_400, on_click=lambda e: handle_note(self.form))
            ]
        )
        
        self.controls.append(self.form)
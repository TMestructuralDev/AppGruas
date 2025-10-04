import flet as ft
from utils.date_picker import date_picker_button
from utils.time_picker import time_picker_button

class NoteForm(ft.Column):
    def __init__(self, page: ft.Page, form_data=None):
        super().__init__(expand=True, spacing=10, scroll=ft.ScrollMode.ALWAYS)
        
        self.fecha_field = ft.TextField(label="Fecha", hint_text="Selecciona una fecha", value=form_data.get("fecha") if form_data else "")
        fecha_button = date_picker_button(page, self.fecha_field)
        
        self.salida_field = ft.TextField(label="Salida", hint_text="Selecciona hora de salida", value=form_data.get("salida") if form_data else "")
        self.llegada_field = ft.TextField(label="Llegada", hint_text="Selecciona hora de llegada", value=form_data.get("llegada") if form_data else "")
        self.termino_field = ft.TextField(label="Termino", hint_text="Selecciona hora de término", value=form_data.get("termino") if form_data else "")
        self.retorno_field = ft.TextField(label="Retorno", hint_text="Selecciona hora de retorno", value=form_data.get("retorno") if form_data else "")
        salida_button = time_picker_button(page, self.salida_field, label="Seleccionar Salida")
        llegada_button = time_picker_button(page, self.llegada_field, label="Seleccionar Llegada")
        termino_button = time_picker_button(page, self.termino_field, label="Seleccionar Término")
        retorno_button = time_picker_button(page, self.retorno_field, label="Seleccionar Retorno")
        
        

        # Campos del formulario
        self.controls.extend([
            ft.TextField(label="Nombre", hint_text="Nombre", max_length=20, value=form_data.get("nombre") if form_data else ""),
            ft.TextField(label="Telefono", hint_text="Telefono", max_length=10),
            ft.TextField(label="Empresa", hint_text="Empresa", max_length=20),
            
            self.fecha_field,
            fecha_button,
            
            ft.TextField(label="Ubicacion", hint_text="Ubicacion", max_length=50),
            ft.TextField(label="Equipo", hint_text="Equipo", max_length=20),
            ft.TextField(label="Operador", hint_text="Operador", max_length=20, value=form_data.get("operador") if form_data else ""),
            ft.TextField(label="Ayudante", hint_text="Ayudante", max_length=20),
            ft.TextField(label="Trabajo a Realizar", hint_text="Trabajo a Realizar", multiline=True),
            
            self.salida_field,
            salida_button,
            self.llegada_field,
            llegada_button,
            self.termino_field,
            termino_button,
            self.retorno_field,
            retorno_button,
            
            ft.TextField(label="Horas de Trabajo", hint_text="Horas de Trabajo", max_length=10),
            ft.TextField(label="Costo Hr o Maniobra", hint_text="Costo Hr o Maniobra", max_length=10),
            ft.TextField(label="Costo Total", hint_text="Costo Total", max_length=10),
            ft.TextField(label="Costo Total con IVA", hint_text="Costo Total con IVA", max_length=10),
            
            ft.TextField(label="Firma", hint_text="Firma", max_length=20),
        ])

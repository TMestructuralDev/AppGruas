import flet as ft
from components.note_form import NoteForm

class CreateNoteView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 20
        self.expand = True
        self.alignment = ft.alignment.center
        
        self.card = ft.Card(
            content=ft.Container(
                content=ft.Icon(ft.Icons.NOTE_ADD_ROUNDED, size=150, color=ft.Colors.GREEN_400),
                alignment=ft.alignment.center,
                on_click=self.show_form, 
                padding=50
            ),
            width=400,
            height=400,
            elevation=10
        )
        
        # Mostrar tarjeta inicial
        self.content = self.card
    
    def show_form(self, e):
        """Mostrar formulario con botón regresar"""
        self.content = ft.Column([
            ft.TextButton("← Regresar", on_click=self.back_to_card),
            NoteForm(self.page)
        ])
        self.alignment = ft.alignment.top_left
        self.page.update()
    
    def back_to_card(self, e):
        """Regresar a tarjeta - reutiliza la tarjeta existente"""
        self.content = self.card
        self.alignment = ft.alignment.center
        self.page.update()
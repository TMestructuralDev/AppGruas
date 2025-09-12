import flet as ft
from data.sample_notes import SAMPLE_NOTES
from components.widgets.open_note_card import OpenNoteCard

class OpenNotesView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True  
        self.scroll = ft.ScrollMode.ALWAYS  
        
        self.cards = ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Container(
                        content=OpenNoteCard(note),
                        on_click=lambda e, n=note: self.open_note(n)
                    )
                    # ------ FOR DE PRUEBA PARA VER NOTAS ABIERTAS
                    for note in SAMPLE_NOTES if note.get("abierta", False)
                ]
            )
        )

        self.controls.append(self.cards)
        
    # ------- FUNCION DE PRUEBA
    def open_note(self, note_data):
        # Guardamos la nota actual en sesión
        self.page.session.set("nota_actual", note_data)
        # Navegamos al formulario
        self.page.go("/form")
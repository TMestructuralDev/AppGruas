import flet as ft
from components.widgets.open_note_card import OpenNoteCard
from handlers.getopen_handler import handle_open_notes

class OpenNotesView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True  
        self.scroll = ft.ScrollMode.ALWAYS  

        # Traemos las notas abiertas usando el handler
        open_notes = handle_open_notes()

        self.cards = ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[OpenNoteCard(note) for note in open_notes]
            )
        )

        self.controls.append(self.cards)
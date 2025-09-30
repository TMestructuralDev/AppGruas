import flet as ft
from components.widgets.open_note_card import OpenNoteCard
from handlers.getopen_handler import handle_open_notes


class OpenNotesView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.alignment = ft.alignment.top_center

        # Traemos las notas abiertas usando el handler
        open_notes = handle_open_notes()

        # Columna que contiene las tarjetas
        notes_column = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[OpenNoteCard(note) for note in open_notes]
        )

        self.content = notes_column
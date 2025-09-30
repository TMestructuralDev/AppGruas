import flet as ft
from data.sample_notes import SAMPLE_NOTES
from components.widgets.closed_note_card import ClosedNoteCard


class ClosedNotesView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.alignment = ft.alignment.top_center

        # Columna que contiene las tarjetas de notas cerradas
        notes_column = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[ClosedNoteCard(note) for note in SAMPLE_NOTES]
        )

        self.content = notes_column
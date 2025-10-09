import flet as ft
from handlers.note_handler import handler_closed_notes
from components.widgets.closed_note_card import ClosedNoteCard


class ClosedNotesView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.alignment = ft.alignment.top_center

        closed_notes = handler_closed_notes(self.page)

        self.notes_column = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[ClosedNoteCard(note, on_edit=self.open_create_note) for note in closed_notes]
        )

        self.content = self.notes_column
        
    def open_create_note(self, note_data):
        """
        Navega a la vista de edición usando el sistema de rutas
        """
        self.page.session.set("edit_note_data", note_data)
        self.page.go("/create")
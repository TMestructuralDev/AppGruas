import flet as ft
from components.widgets.open_note_card import OpenNoteCard
from views.create_note import CreateNoteView
from handlers.getopen_handler import handle_open_notes

class OpenNotesView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.alignment = ft.alignment.top_center

        open_notes = handle_open_notes()

        self.notes_column = ft.Column(
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[OpenNoteCard(note, on_edit=self.open_create_note) for note in open_notes]
        )

        self.content = self.notes_column

    def open_create_note(self, note_data):
        """
        Abre la vista CreateNoteView con los datos precargados
        """
        create_note_view = CreateNoteView(self.page, form_data=note_data)
        # Reemplazamos la columna de notas por el formulario (puedes usar modal o reemplazo directo)
        self.content = create_note_view
        self.page.update()
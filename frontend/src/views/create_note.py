import flet as ft
from components.widgets.note_form import NoteForm


class CreateNoteView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.alignment = ft.alignment.top_center
        self.padding = 20

        # En vez del Card, usamos directamente el formulario
        self.content = NoteForm(page)
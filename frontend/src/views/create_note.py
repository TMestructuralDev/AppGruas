import flet as ft
from components.widgets.note_form import NoteForm
from handlers.note_handler import handler_open_note

class CreateNoteView(ft.Container):
    def __init__(self, page: ft.Page, form_data=None):
        super().__init__()
        self.expand = True
        self.alignment = ft.alignment.top_center
        self.padding = 20

        # Pasamos form_data al formulario para precargar campos
        #form_data = page.data if page.data else None
        if form_data is None:
            form_data = page.session.get("edit_note_data")
            if form_data:
                page.session.remove("edit_note_data")
                
        self.form = NoteForm(page, form_data=form_data)

        open_button = ft.ElevatedButton(
            "Abrir Nota",
            icon=ft.Icons.NOTE_ADD_OUTLINED,
            icon_color=ft.Colors.GREEN_400,
            on_click=lambda e: handler_open_note(self.form, page)
        )

        self.form.controls.append(open_button)
        self.content = self.form
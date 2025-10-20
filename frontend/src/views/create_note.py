import flet as ft
from components.widgets.note_form import NoteForm
from handlers.note_handler import handler_open_note, handler_send_note

class CreateNoteView(ft.Container):
    def __init__(self, page: ft.Page, form_data=None):
        super().__init__()
        self.expand = True
        self.alignment = ft.alignment.top_center
        self.padding = 20

        
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
        
        send_button = ft.ElevatedButton(
            "Enviar Nota",
            icon=ft.Icons.SEND_TO_MOBILE_OUTLINED,
            icon_color=ft.Colors.GREEN_400,
            on_click=lambda e: handler_send_note(self.form, page)
        )

        self.form.controls.append(open_button)
        self.form.controls.append(send_button)
        
        self.content = self.form
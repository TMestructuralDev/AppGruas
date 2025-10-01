import flet as ft
from components.widgets.note_form import NoteForm
from handlers.note_handler import handler_open_note


class CreateNoteView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True
        self.alignment = ft.alignment.top_center
        self.padding = 20

        # En vez del Card, usamos directamente el formulario
        self.form = NoteForm(page)

        # Creamos el botón
        open_button = ft.ElevatedButton(
            "Abrir Nota",
            icon=ft.Icons.NOTE_ADD_OUTLINED,
            icon_color=ft.Colors.GREEN_400,
            on_click=lambda e: handler_open_note(self.form, page)
        )

        # Solo agregamos el botón al final de la columna del formulario
        self.form.controls.append(open_button)

        # El contenido del contenedor es solo el form
        self.content = self.form

        
   
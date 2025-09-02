import flet as ft
from data.sample_notes import SAMPLE_NOTES
from components.note_card import create_note_card

class OpenNotesView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        
        self.controls.append(ft.Text("Notas Abiertas", size=20, weight=ft.FontWeight.BOLD))
        
        for note in SAMPLE_NOTES:
            self.controls.append(create_note_card(note))
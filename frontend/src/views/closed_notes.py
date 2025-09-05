import flet as ft
from data.sample_notes import SAMPLE_NOTES
from components.closed_note_card import ClosedNoteCard

class ClosedNotesView(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.expand = True  
        self.scroll = ft.ScrollMode.ALWAYS  
        
        self.cards = ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,  
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[ClosedNoteCard(note) for note in SAMPLE_NOTES]
            )
        )

        self.controls.append(self.cards)
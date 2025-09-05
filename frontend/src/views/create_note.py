import flet as ft

class CreateNoteView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 20
        self.expand = True
        self.alignment = ft.alignment.center
        
        # Tarjeta inicial
        self.content = ft.Card(
            content=ft.Container(
                content=ft.Icon(
                    ft.Icons.NOTE_ADD_ROUNDED,
                    size=150,
                    color=ft.Colors.PINK_ACCENT_400
                ),
                alignment=ft.alignment.center,
                padding=50,
                on_click=lambda e: self.page.go("/form")  
            ),
            width=400,
            height=400,
            elevation=10
        )

        
        
    
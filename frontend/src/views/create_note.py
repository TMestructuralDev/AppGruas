import flet as ft

class CreateNoteView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 20
        self.expand = True
        self.alignment = ft.alignment.center

        # Tarjeta inicial con icono y texto
        self.content = ft.Card(
            width=400,
            height=400,
            elevation=10,
            clip_behavior= ft.ClipBehavior.ANTI_ALIAS,
            content=ft.Container(
                padding=50,
                alignment=ft.alignment.center,
                content=ft.Column(
                    controls=[
                        ft.Icon(
                            ft.Icons.NOTE_ADD_ROUNDED,
                            size=150,
                            color=ft.Colors.PINK_ACCENT_400
                        ),
                        ft.Text(
                            "Nueva Nota",
                            size=24,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
            on_click=lambda e: self.page.go("/form")
            ),
        )
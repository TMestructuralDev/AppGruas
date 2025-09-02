import flet as ft 

class Bottom(ft.BottomAppBar):
    def __init__(self): 
        super().__init__()
        self.bgcolor = ft.Colors.BLACK
        self.shape = ft.NotchShape.CIRCULAR
        
        self.content = ft.Row(
            controls=[
                ft.ElevatedButton(
                    "Crear",
                    icon=ft.Icons.NOTE_ADD_ROUNDED,
                    icon_color=ft.Colors.PINK_ACCENT_400,
                    style=ft.ButtonStyle(color=ft.Colors.WHITE),
                    expand=True,
                    on_click=lambda e: self.page.go("/create")
                ),
                ft.ElevatedButton(
                    "Abiertas",
                    icon=ft.Icons.EDIT_NOTE,
                    icon_color=ft.Colors.GREEN_400,
                    style=ft.ButtonStyle(color=ft.Colors.WHITE),
                    expand=True,
                    on_click=lambda e: self.page.go("/open")
                ),
                ft.ElevatedButton(
                    "Cerradas",
                    icon=ft.Icons.STICKY_NOTE_2_ROUNDED,
                    icon_color=ft.Colors.DEEP_ORANGE_500,
                    style=ft.ButtonStyle(color=ft.Colors.WHITE),
                    expand=True,
                    on_click=lambda e: self.page.go("/closed")
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
            spacing=10, 
        )
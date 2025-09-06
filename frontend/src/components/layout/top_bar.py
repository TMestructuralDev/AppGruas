import flet as ft

class Top(ft.AppBar):
    def __init__(self):
        super().__init__()
        self.title=ft.Text("TM GRUAS")
        self.bgcolor=ft.Colors.BLACK
        
        self.actions=[
            ft.TextButton(
            "ADMIN",
            icon=ft.Icons.ADMIN_PANEL_SETTINGS_ROUNDED,
            icon_color=ft.Colors.PINK_400,
        ),
        ]
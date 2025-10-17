import flet as ft
from theme.colors import COLORS

class Top(ft.AppBar):
    def __init__(self):
        super().__init__()
        self.title=ft.Text("TM GRUAS")
        self.bgcolor= COLORS['top_bar_color']
        
        self.actions=[
            ft.TextButton(
            "ADMIN",
            icon=ft.Icons.ADMIN_PANEL_SETTINGS_ROUNDED,
            icon_color=ft.Colors.PINK_400,
        ),
        ]
        
        # self.actions = [get_session_button(self.page)]
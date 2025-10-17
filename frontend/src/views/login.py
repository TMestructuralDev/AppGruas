import flet as ft
from handlers.auth_handler import handler_login

class LoginView(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.username = ft.TextField(label="Usuario")
        self.password = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
        self.login_button = ft.ElevatedButton(
            "Iniciar sesión",
            icon=ft.Icons.LOGIN,
            on_click=self.on_login_click
        )

        self.content = ft.Column(
            [
                ft.Text("Iniciar sesión", size=24, weight="bold"),
                self.username,
                self.password,
                self.login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def on_login_click(self, e):
        credentials = {
            "username": self.username.value,
            "password": self.password.value,
        }
        handler_login(self.page, credentials)
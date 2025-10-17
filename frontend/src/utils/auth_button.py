import flet as ft
from handlers.session_handler import handler_check_session, handler_logout

def get_session_button(page: ft.Page):
    """Devuelve el botón adecuado según el estado de sesión."""
    if handler_check_session():
        return ft.TextButton(
            "LOGOUT",
            icon=ft.Icons.LOGOUT,
            icon_color=ft.Colors.RED_400,
            on_click=lambda e: confirm_logout(page)
        )
    else:
        return ft.TextButton(
            "LOGIN",
            icon=ft.Icons.LOGIN,
            icon_color=ft.Colors.GREEN_400,
            on_click=lambda e: page.go("/login")
        )


def confirm_logout(page: ft.Page):
    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("¿Cerrar sesión?"),
        content=ft.Text("¿Deseas salir de tu cuenta actual?"),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda e: close_dialog(page, dlg)),
            ft.TextButton("Cerrar sesión", on_click=lambda e: do_logout(page, dlg))
        ]
    )
    page.dialog = dlg
    dlg.open = True
    page.update()


def close_dialog(page: ft.Page, dlg: ft.AlertDialog):
    dlg.open = False
    page.update()


def do_logout(page: ft.Page, dlg: ft.AlertDialog):
    dlg.open = False
    handler_logout(page)
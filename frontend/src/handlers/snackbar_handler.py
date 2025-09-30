import flet as ft

def show_snack(page: ft.Page, message: str, success: bool = True, duration: int = 4000):
    """
    Muestra un SnackBar en la página.
    - success=True → color verde, mensaje de éxito.
    - success=False → color rojo, mensaje de error.
    """
    snack = ft.SnackBar(
        content=ft.Text(message),
        bgcolor=ft.Colors.GREEN if success else ft.Colors.RED,
        open=True
    )
    page.overlay.append(snack)  # lo agregamos directamente a la UI
    page.update()
from usecases.login_usecase import LoginUseCase
import flet as ft

def handler_login(page, credentials):
    """
    El handler solo orquesta la interacción con el caso de uso.
    """
    try:
        user = LoginUseCase.execute(credentials)
        page.snack_bar = ft.SnackBar(ft.Text(f"Bienvenido {user['username']}"))
        page.snack_bar.open = True
        page.go("/home")
    except Exception as e:
        page.snack_bar = ft.SnackBar(ft.Text(f"Error al iniciar sesión: {e}"))
        page.snack_bar.open = True
    finally:
        page.update()
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import flet as ft
from controllers.router import Router
from theme.colors import COLORS

def main(page: ft.Page):
    page.title = "Sistema de Notas"
    
    page.snack_bar = ft.SnackBar(
        content=ft.Text(""),        # contenido inicial vacío
        bgcolor=ft.Colors.GREEN_400 # color inicial opcional
    )
    page.update()

    # Inicializar el router
    router = Router(page)
    
    # Navegar a la ruta inicial
    page.go(page.route)

ft.app(main)
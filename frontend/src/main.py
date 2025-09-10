import flet as ft
from controllers.router import Router

def main(page: ft.Page):
    page.title = "Sistema de Notas"
    page.bgcolor = "#121212"
    
    # Inicializar el router
    router = Router(page)
    
    # Navegar a la ruta inicial
    page.go(page.route)

ft.app(main)
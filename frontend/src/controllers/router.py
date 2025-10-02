import flet as ft
from urls.routes import get_view_for_route

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop

        # Navegar a la ruta inicial
        self.page.go(self.page.route)

    def route_change(self, e: ft.RouteChangeEvent):
        """Construye la vista correspondiente a la ruta actual"""
        if e.route == "/open":
            self.page.views.clear()
            
        view = get_view_for_route(self.page.route, self.page)
        self.page.views.append(view)
        self.page.update()

    def view_pop(self, view: ft.View):
        """Maneja la acción de 'regresar'"""
        self.page.views.pop() if self.page.views else None
    
        # ir a la vista anterior o fallback
        target_route = self.page.views[-1].route if self.page.views else "/open"
        self.page.go(target_route)
        self.page.update()

    
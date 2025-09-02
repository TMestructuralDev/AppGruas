import flet as ft
from routes import get_view_for_route

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.setup_navigation()
    
    def setup_navigation(self):
        """Configura los manejadores de navegación"""
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
    
    def route_change(self, route):
        """Maneja los cambios de ruta"""
        self.page.views.clear()
        
        # Obtener vista para la ruta actual
        view = get_view_for_route(self.page.route, self.page)
        
        if view:
            self.page.views.append(view)
        else:
            # Ruta no encontrada, ir al inicio
            self.page.views.append(get_view_for_route("/open", self.page))
        
        self.page.update()
    
    def view_pop(self, view):
        """Maneja el botón de regresar"""
        self.page.views.pop()
        
        if self.page.views:
            top_view = self.page.views[-1]
            self.page.go(top_view.route)
        else:
            # Si no hay vistas, ir al inicio
            self.page.go("/open")
    
    def navigate_to(self, route):
        """Navega a una ruta específica"""
        self.page.go(route)
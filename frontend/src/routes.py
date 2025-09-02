import flet as ft
from components.top_bar import Top
from components.bottom_bar import Bottom
from views.create_note import CreateNoteView
from views.open_notes import OpenNotesView

def get_view_for_route(route: str, page: ft.Page) -> ft.View:
    """
    Retorna la vista correspondiente a una ruta
    """
    
    if route == "/create":
        return ft.View(
            route="/create",
            controls=[
                Top(),
                CreateNoteView(page),
                Bottom()
            ]
        )
    
    elif route == "/open":
        return ft.View(
            route="/open",
            controls=[
                Top(),
                OpenNotesView(page),
                Bottom()
            ]
        )
    
    elif route == "/closed":
        return ft.View(
            route="/closed",
            controls=[
                Top(),
                ft.Text("Vista de Notas Cerradas - Por implementar", size=20),
                Bottom()
            ]
        )
    
    else:
        
        return ft.View(
            route="/open",
            controls=[
                Top(),
                OpenNotesView(page),
                Bottom()
            ]
        )
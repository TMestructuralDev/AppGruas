import flet as ft
from components.layout.top_bar import Top
from components.layout.bottom_bar import Bottom
from components.widgets.note_form import NoteForm
from views.create_note import CreateNoteView
from views.open_notes import OpenNotesView
from views.closed_notes import ClosedNotesView
from theme.colors import COLORS


    
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
      
    elif route == "/form":
        return ft.View(
            route="/form",
            controls=[
                Top(),
                NoteForm(page),
                Bottom()
            ]
        )
    
    
    elif route == "/open":
        return ft.View(
            route="/open",
            bgcolor=COLORS["main_bg_color"],
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
                ClosedNotesView(page),
                Bottom()
            ]
        )
    
    else:
        
        return ft.View(
            route="/open",
            bgcolor=COLORS["main_bg_color"],
            controls=[
                Top(),
                OpenNotesView(page),
                Bottom()
            ]
        )
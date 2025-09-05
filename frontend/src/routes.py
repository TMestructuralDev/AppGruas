import flet as ft
from components.top_bar import Top
from components.bottom_bar import Bottom
from components.note_form import NoteForm
from views.create_note import CreateNoteView
from views.open_notes import OpenNotesView
from views.closed_notes import ClosedNotesView

    
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
                #ft.TextButton("← Regresar", on_click=lambda e: page.on_view_pop(page.views)),
                NoteForm(page),
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
                ClosedNotesView(page),
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
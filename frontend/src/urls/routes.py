import flet as ft
from components.layout.top_bar import Top
from components.layout.bottom_bar import Bottom
from components.widgets.note_form import NoteForm
from views.create_note import CreateNoteView
from views.open_notes import OpenNotesView
from views.closed_notes import ClosedNotesView
from theme.colors import COLORS


def get_view_for_route(route: str, page: ft.Page) -> ft.View:

    routes = {
        "/create": CreateNoteView,
        "/form": NoteForm,
        "/open": OpenNotesView,
        "/closed": ClosedNotesView,
    }

    
    view_route = routes.get(route, OpenNotesView)

    return ft.View(
        route=route if route in routes else "/open",
        bgcolor=COLORS["main_bg_color"],
        controls=[
            Top(),
            view_route(page),
            Bottom()
        ]
    )
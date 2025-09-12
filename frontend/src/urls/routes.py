import flet as ft
from components.layout.top_bar import Top
from components.layout.bottom_bar import Bottom
from components.widgets.note_form import NoteForm
from views.create_note import CreateNoteView
from views.open_notes import OpenNotesView
from views.closed_notes import ClosedNotesView

    
def get_view_for_route(route: str, page: ft.Page) -> ft.View:
    """
    Retorna la vista correspondiente a una ruta
    """
    
    if route == "/create":
        # ------ REMOVER NOTA PARA PRUEBA
        page.session.remove("nota_actual") # <----
        return ft.View(
            route="/create",
            controls=[
                Top(),
                CreateNoteView(page),
                Bottom()
            ]
        )
      
    #elif route == "/form":
     #   return ft.View(
      #      route="/form",
       #     controls=[
        #        Top(),
         #       NoteForm(page),
          #      Bottom()
           # ]
        #)
    
    # -------- FORMULARIO DE NOTAS DE PRUEBA     
    elif route == "/form":
        note = page.session.get("nota_actual")  # <-- obtiene la nota seleccionada
        return ft.View(
            route="/form",
            controls=[
                Top(),
                NoteForm(page, note=note),  # <-- pasa la nota al formulario
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
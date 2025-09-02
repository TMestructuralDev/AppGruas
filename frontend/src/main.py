'''import flet as ft
from components.bottom_bar import Bottom
from components.top_bar import Top
from views.create_note import CreateNoteView
from views.open_notes import OpenNotesView



def main(page: ft.Page):
    
    page.add(Top())
    
    #page.add(CreateNoteView(page))
    
    page.add(OpenNotesView(page))
    
    page.add(Bottom())



ft.app(main)'''

import flet as ft
from router import Router

def main(page: ft.Page):
    page.title = "Sistema de Notas"
    
    # Inicializar el router
    router = Router(page)
    
    # Navegar a la ruta inicial
    page.go(page.route)

ft.app(main)
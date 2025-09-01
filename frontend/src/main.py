import flet as ft
from components.bottom_bar import Bottom
from components.top_bar import Top
from views.create_note import CreateNoteView



def main(page: ft.Page):
    
    page.add(Top())
    
    #create_view = Create(page)
    #page.add(create_view.get_controls())
    page.add(CreateNoteView(page))
    
    page.add(Bottom())



ft.app(main)

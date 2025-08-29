import flet as ft
from components.bottom_bar import Bottom
from components.top_bar import Top
from views.create_note import Create



def main(page: ft.Page):
    
    page.add(Top())
    
    page.add(Create(page))
    
    page.add(Bottom())



ft.app(main)

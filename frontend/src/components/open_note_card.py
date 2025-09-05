import flet as ft

class OpenNoteCard(ft.Card):
    def __init__(self, note_data):
        super().__init__()
        #self.bgcolor = ft.Colors.GREEN_800
        self.color = ft.Colors.GREEN_800
        self.border_radius = 10
        self.elevation = 3
        
        self.content=ft.Column(
                controls=[
                    ft.Text(f"{note_data['operador']}", size=14, text_align=ft.TextAlign.CENTER),
                    ft.Text(f"{note_data['ayudante']}", size=14, text_align=ft.TextAlign.CENTER),
                    ft.Text(f"{note_data['empresa']}", size=12, text_align=ft.TextAlign.CENTER),
                    ft.Text(f"Ubicación: {note_data['ubicacion']}", size=12, text_align=ft.TextAlign.CENTER),
                    ft.Text(f"Hora de Llegada: {note_data['llegada']}", size=12, text_align=ft.TextAlign.CENTER),
                    ft.Text(f"Fecha: {note_data['fecha']}", size=12, text_align=ft.TextAlign.CENTER),
                    ft.Text(f"Equipo: {note_data['equipo']}", size=12, text_align=ft.TextAlign.CENTER),
                ],
                spacing=5,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
            
            
            
        

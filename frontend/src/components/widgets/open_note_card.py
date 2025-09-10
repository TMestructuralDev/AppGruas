import flet as ft

class OpenNoteCard(ft.Card):
    def __init__(self, note_data):
        super().__init__()
        
        self.bgcolor = "#1E1E1E"
        self.border_radius = 16
        self.elevation = 6
        self.width = 260
        #elf.height = 280
        self.shadow_color = ft.Colors.with_opacity(0.3, "#2BD10A")
        self.clip_behavior = ft.ClipBehavior.ANTI_ALIAS
        
        self.content=ft.Column(
            expand=True,
            controls=[
                ft.Text(note_data["operador"], size=18, weight="bold", color="white", text_align=ft.TextAlign.CENTER),
                ft.Text(note_data["ayudante"], size=14, weight="w500", color="white", text_align=ft.TextAlign.CENTER),
                ft.Text(note_data["empresa"], size=13, color="#B0B0B0", text_align=ft.TextAlign.CENTER),
                ft.Text(f"{note_data['ubicacion']}", size=12, color="#B0B0B0", text_align=ft.TextAlign.CENTER),
                ft.Text(f"{note_data['llegada']}", size=12, color="#B0B0B0", text_align=ft.TextAlign.CENTER),
                ft.Text(f"{note_data['fecha']}", size=12, color="#B0B0B0", text_align=ft.TextAlign.CENTER),
                ft.Text(f"{note_data['equipo']}", size=12, color="#B0B0B0", text_align=ft.TextAlign.CENTER),
                ft.Divider(height=10, thickness=1, color="#2C2C2C"),
                ft.Row([
                    
                    ft.IconButton(ft.Icons.EDIT_DOCUMENT, icon_color="#90A4AE"),
                    ft.IconButton(ft.Icons.DELETE_FOREVER, icon_color="#F44336"),
                    ], 
                #tight= True,
                alignment = ft.MainAxisAlignment.SPACE_EVENLY
                )
    ],
    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
)

    
            
        

import flet as ft
from theme.colors import COLORS

class ClosedNoteCard(ft.Card):
    def __init__(self, note_data):
        super().__init__()

        self.bgcolor = "#1E1E1E"
        self.surface_tint_color = "#2A2A2A"
        self.border_radius = 8
        self.elevation = 12
        self.width = 320
        self.shadow_color = ft.Colors.with_opacity(0.3, "#F44336")
        self.clip_behavior = ft.ClipBehavior.ANTI_ALIAS

        self.content = ft.Column(
            expand=True,
            controls=[
                ft.Text(note_data["operador"], size=18, weight="bold", color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data["ayudante"], size=14, weight="w500", color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data["empresa"], size=13, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(f"{note_data['ubicacion']}", size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(f"{note_data['llegada']}", size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(f"{note_data['fecha']}", size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(f"{note_data['equipo']}", size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Divider(height=10, thickness=1, color=COLORS['card_divider_color']),
                ft.Row([
                
                    ft.IconButton(ft.Icons.DOWNLOAD, icon_color="#90A4AE"),
                    ft.IconButton(ft.Icons.EDIT_DOCUMENT, icon_color="#90A4AE"),
                    ft.IconButton(ft.Icons.DELETE_FOREVER, icon_color="#F44336"),
                ],
                #tight= True,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

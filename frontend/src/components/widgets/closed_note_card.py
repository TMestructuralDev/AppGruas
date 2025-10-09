import flet as ft
from theme.colors import COLORS

class ClosedNoteCard(ft.Card):
    def __init__(self, note_data, on_edit=None, on_delete=None):
        super().__init__()
        self.note_data = note_data
        self.on_edit = on_edit
        self.on_delete = on_delete

        self.bgcolor = "#1E1E1E"
        self.surface_tint_color = "#2A2A2A"
        self.border_radius = 8
        self.elevation = 12
        self.width = 320
        self.shadow_color = ft.Colors.with_opacity(0.3, "#F44336")
        self.clip_behavior = ft.ClipBehavior.ANTI_ALIAS

        self.content = ft.Column(
            expand=True,
            spacing=8,
            controls=[
                ft.Text(note_data.get("nombre", ""), size=20, weight="bold", color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data.get("operador", ""), size=12, weight="bold", color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data.get("ayudante", ""), size=12, weight="w500", color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data.get("empresa", ""), size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data.get("ubicacion", ""), size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data.get("llegada", ""), size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data.get("fecha", ""), size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Text(note_data.get("equipo", ""), size=12, color=COLORS['card_text_color'], text_align=ft.TextAlign.CENTER),
                ft.Divider(height=10, thickness=1, color=COLORS['card_divider_color']),
                ft.Row([
                    ft.IconButton(
                        ft.Icons.EDIT_DOCUMENT,
                        icon_color="#90A4AE",
                        on_click=lambda e: self.on_edit(self.note_data) if self.on_edit else None
                    ),
                    ft.IconButton(
                        ft.Icons.DELETE_FOREVER,
                        icon_color="#F44336",
                        on_click=lambda e: self.on_delete(self.note_data) if self.on_delete else None
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

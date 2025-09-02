import flet as ft

def create_note_card(note_data):
    return ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text(f"Nota #{note_data['id']}", size=16, weight=ft.FontWeight.BOLD),
                ft.Text(f"{note_data['nombre']}", size=14),
                ft.Text(f"{note_data['empresa']}", size=12),
                ft.Text(f"Fecha: {note_data['fecha']}", size=12),
                ft.Text(f"Equipo: {note_data['equipo']}", size=12),
            ], spacing=5),
            padding=15
        )
    )
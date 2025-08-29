import flet as ft
import flet.canvas as cv

class SignatureState:
    x: float
    y: float

_state = SignatureState()

def create_signature_canvas(width: int = 300, height: int = 150) -> ft.Container:
    """
    Canvas para dibujar a mano alzada, dentro de un container para limitar tamaño.
    """
    def pan_start(e: ft.DragStartEvent):
        _state.x = e.local_x
        _state.y = e.local_y

    def pan_update(e: ft.DragUpdateEvent):
        canvas.shapes.append(
            cv.Line(
                _state.x,
                _state.y,
                e.local_x,
                e.local_y,
                paint=ft.Paint(stroke_width=2, color=ft.Colors.BLACK),
            )
        )
        canvas.update()
        _state.x = e.local_x
        _state.y = e.local_y

    canvas = cv.Canvas(
        shapes=[cv.Fill(ft.Paint(color=ft.Colors.WHITE))],
        content=ft.GestureDetector(
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            drag_interval=1,
        ),
        width=width,
        height=height,
    )

    # Container para limitar tamaño y agregar borde
    container = ft.Container(
        content=canvas,
        width=width,
        height=height,
        border=ft.border.all(1, ft.Colors.BLACK),
        border_radius=5,
    )

    return container

def clear_canvas(container: ft.Container):
    """Limpia el canvas dentro del container"""
    canvas = container.content
    canvas.shapes.clear()
    canvas.shapes.append(cv.Fill(ft.Paint(color=ft.Colors.WHITE)))
    canvas.update()

import flet as ft

def extract_note_data(form_column: ft.Column) -> dict:
    """
    Extrae todos los datos de un formulario basado en TextField.
    Fecha y horas ya vienen en formato correcto (YYYY-MM-DD / HH:MM),
    así que no hace falta parsearlas.
    """
    data = {}

    for control in form_column.controls:
        if isinstance(control, ft.TextField):
            key = control.label.lower().replace(" ", "_")
            value = control.value.strip() if control.value else None
            data[key] = value
    return data




def extract_open_note_data(form_column):
    data = {}
    for control in form_column.controls:
        if isinstance(control, ft.TextField):
            label = control.label.strip().lower()
            if label == "nombre":
                data["nombre"] = control.value or None
            elif label == "operador":
                data["operador"] = control.value or None
            elif label == "fecha":
                data["fecha"] = control.value or None
    return data
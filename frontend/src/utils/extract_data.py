from flet import Column, TextField, DatePicker, TimePicker
import flet as ft

def extract_data(form_column: Column) -> dict:
    data = {}

    for control in form_column.controls:
        # TextField
        if isinstance(control, TextField):
            key = control.label.lower().replace(" ", "_")
            data[key] = control.value if control.value != "" else None

        # DatePicker
        elif isinstance(control, DatePicker):
            key = control.label.lower().replace(" ", "_")
            if control.value is not None:
                data[key] = control.value.strftime("%Y-%m-%d")
            else:
                data[key] = None

        # TimePicker
        elif isinstance(control, TimePicker):
            key = control.label.lower().replace(" ", "_")
            if control.value is not None:
                data[key] = control.value.strftime("%H:%M")
            else:
                data[key] = None


    return data


def extract_open_note_data(form_column):
    """
    Extrae solo los datos necesarios para abrir una nota:
    nombre, fecha y operador
    """
    data = {}
    for control in form_column.controls:
        if isinstance(control, ft.TextField):
            if control.label == "Nombre":
                data["nombre"] = control.value
            elif control.label == "Operador":
                data["operador"] = control.value
        elif isinstance(control, ft.Row) and hasattr(control, "value") and control.value is not None:
            data["fecha"] = control.value.isoformat() 
    return data
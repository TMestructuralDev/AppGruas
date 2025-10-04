from datetime import date

def build_open_payload(form_data: dict) -> dict:
    """
    Adapter para abrir una nota.
    Convierte fecha a string ISO.
    """
    fecha = form_data.get("fecha")
    if isinstance(fecha, date):
        fecha = fecha.isoformat()

    return {
        "nombre": form_data.get("nombre"),
        "fecha": fecha,
        "operador": form_data.get("operador"),
    }
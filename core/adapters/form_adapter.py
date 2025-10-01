from datetime import date

def build_payload(form_data: dict) -> dict:
    """
    Adapter para enviar todos los datos de la nota al backend.
    Convierte fechas a string y asegura que los campos opcionales puedan ser None.
    """
    # Convertir fecha y tiempos a string si son datetime.date o datetime.time
    fecha = form_data.get("fecha")
    if isinstance(fecha, date):
        fecha = fecha.isoformat()

    # Lo mismo para tiempos, si los tienes
    salida = form_data.get("salida")
    llegada = form_data.get("llegada")
    termino = form_data.get("termino")
    retorno = form_data.get("retorno")

    def time_to_str(t):
        return t.strftime("%H:%M") if t is not None else None

    return {
        "nombre": form_data.get("nombre"),
        "telefono": form_data.get("telefono"),
        "empresa": form_data.get("empresa"),
        "fecha": fecha,
        "ubicacion": form_data.get("ubicacion"),
        "equipo": form_data.get("equipo"),
        "operador": form_data.get("operador"),
        "ayudante": form_data.get("ayudante"),
        "trabajo_realizar": form_data.get("trabajo_realizar"),

        # Tiempos convertidos a string
        "salida": time_to_str(salida),
        "llegada": time_to_str(llegada),
        "termino": time_to_str(termino),
        "retorno": time_to_str(retorno),
        "total_horas": form_data.get("total_horas"),

        # Costos
        "costo_hora": form_data.get("costo_hora"),
        "costo_total": form_data.get("costo_total"),
        "costo_total_iva": form_data.get("costo_total_iva"),

        # Firma cliente (opcional)
        "firma_cliente": form_data.get("firma_cliente", None),

        # Estado por defecto
        "nota_abierta": True,
    }


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
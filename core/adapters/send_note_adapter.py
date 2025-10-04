def send_note_payload(form_data: dict) -> dict:
    """
    Adapter para enviar los datos de la nota al backend.
    Convierte los campos numéricos a float y limpia los strings.
    Hace mapeo de nombres del front al modelo Django.
    """
    def clean_str(value):
        """Convierte strings vacíos en None y elimina espacios extra."""
        if isinstance(value, str):
            value = value.strip()
            return value if value else None
        return value

    def to_float(value):
        """Convierte a float si aplica, sino None."""
        try:
            return float(value) if value not in (None, "", " ") else None
        except (ValueError, TypeError):
            return None

    return {
        # Strings directos
        "nombre": clean_str(form_data.get("nombre")),
        "telefono": clean_str(form_data.get("telefono")),
        "empresa": clean_str(form_data.get("empresa")),
        "fecha": clean_str(form_data.get("fecha")),   # ya viene como string "YYYY-MM-DD"
        "ubicacion": clean_str(form_data.get("ubicacion")),
        "equipo": clean_str(form_data.get("equipo")),
        "operador": clean_str(form_data.get("operador")),
        "ayudante": clean_str(form_data.get("ayudante")),
        "trabajo_realizar": clean_str(form_data.get("trabajo_a_realizar")),

        # Tiempos (ya vienen como string "HH:MM" o "HH:MM:SS")
        "salida": clean_str(form_data.get("salida")),
        "llegada": clean_str(form_data.get("llegada")),
        "termino": clean_str(form_data.get("termino")),
        "retorno": clean_str(form_data.get("retorno")),

        # Totales / costos convertidos a float
        "total_horas": to_float(form_data.get("horas_de_trabajo")),
        "costo_hora": to_float(form_data.get("costo_hr_o_maniobra")),
        "costo_total": to_float(form_data.get("costo_total")),
        "costo_total_iva": to_float(form_data.get("costo_total_con_iva")),

        # Firma
        "firma_cliente": clean_str(form_data.get("firma")),

        # Estado por defecto
        "nota_abierta": True,
    }

def send_note_payload(form_data: dict) -> dict:
    """
    Convierte campos numéricos a float y deja strings tal cual.
    No elimina nada que tenga valor, conserva 0 como válido.
    """
    def clean_str(value):
        """Elimina espacios extra de strings, devuelve None si es vacío o None."""
        if isinstance(value, str):
            value = value.strip()
            return value if value else None
        return value

    def to_float(value):
        """
        Convierte a float si es posible.
        Devuelve None solo si es None o string vacío.
        Conserva 0 como valor válido.
        """
        if value is None:
            return None
        if isinstance(value, str) and value.strip() == "":
            return None
        try:
            return float(value)
        except (ValueError, TypeError):
            return None

    return {
        # Strings directos
        "nombre": clean_str(form_data.get("nombre")),
        "telefono": clean_str(form_data.get("telefono")),
        "empresa": clean_str(form_data.get("empresa")),
        "fecha": clean_str(form_data.get("fecha")),
        "ubicacion": clean_str(form_data.get("ubicacion")),
        "equipo": clean_str(form_data.get("equipo")),
        "operador": clean_str(form_data.get("operador")),
        "ayudante": clean_str(form_data.get("ayudante")),
        "trabajo_realizar": clean_str(form_data.get("trabajo_a_realizar")),

        # Tiempos
        "salida": clean_str(form_data.get("salida")),
        "llegada": clean_str(form_data.get("llegada")),
        "termino": clean_str(form_data.get("termino")),
        "retorno": clean_str(form_data.get("retorno")),

        # Numéricos
        "total_horas": to_float(form_data.get("horas_de_trabajo")),
        "costo_hora": to_float(form_data.get("costo_hr_o_maniobra")),
        "costo_total": to_float(form_data.get("costo_total")),
        "costo_total_iva": to_float(form_data.get("costo_total_con_iva")),

        # Firma
        "firma_cliente": clean_str(form_data.get("firma")),

        # Estado por defecto
        "nota_abierta": True,
    }

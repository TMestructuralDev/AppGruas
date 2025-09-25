def build_payload(form_data: dict) -> dict:
    
    return {
        "nombre": form_data.get("nombre"),
        "telefono": form_data.get("telefono"),
        "empresa": form_data.get("empresa"),
        "fecha": form_data.get("fecha"),
        "ubicacion": form_data.get("ubicacion"),
        "equipo": form_data.get("equipo"),
        "operador": form_data.get("operador"),
        "ayudante": form_data.get("ayudante"),
        "trabajo_realizar": form_data.get("trabajo_realizar"),

        # Tiempos
        "salida": form_data.get("salida"),
        "llegada": form_data.get("llegada"),
        "termino": form_data.get("termino"),
        "retorno": form_data.get("retorno"),
        "total_horas": form_data.get("total_horas"),

        # Costos
        "costo_hora": form_data.get("costo_hora"),
        "costo_total": form_data.get("costo_total"),
        "costo_total_iva": form_data.get("costo_total_iva"),

        # Firma cliente (temporal, por ejemplo nombre)
        "firma_cliente": form_data.get("firma_cliente", None),

        # Estado por defecto
        "nota_abierta": True,
    }
    
    
''' Adapter for opening notes '''

def build_open_payload(form_data: dict) -> dict:
    return {
        "nombre": form_data.get("nombre"),
        "fecha": form_data.get("fecha"),
        "operador": form_data.get("operador"),

    }
from datetime import datetime

def calculate_note_totals(form_data: dict) -> dict:
    """
    Calcula:
    - total de horas trabajadas (en horas decimales)
    - costo_total
    - costo_total_con_iva (16%)
    A partir de las horas seleccionadas en el formulario.
    """
    fmt = "%H:%M:%S"

    # Extraer horas del formulario
    salida = form_data.get("salida")
    retorno = form_data.get("retorno")

    total_horas = 0.0

    try:
        if salida and retorno:
            salida_dt = datetime.strptime(salida, fmt)
            retorno_dt = datetime.strptime(retorno, fmt)

            diff = retorno_dt - salida_dt
            total_horas = diff.total_seconds() / 3600  # horas decimales

            if total_horas < 0:
                # Caso: la jornada pasa de medianoche (00:00)
                total_horas += 24
    except Exception as e:
        print(f"[WARN] Error calculando horas: {e}")

    # Calcular costos
    try:
        costo_hora = float(form_data.get("costo_hr_o_maniobra", 0))
    except ValueError:
        costo_hora = 0.0

    costo_total = round(total_horas * costo_hora, 2)
    costo_total_con_iva = round(costo_total * 1.16, 2)

    # Retornar diccionario con cálculos
    return {
        "horas_de_trabajo": total_horas,
        "costo_hora": costo_hora,
        "costo_total": costo_total,
        "costo_total_con_iva": costo_total_con_iva,
    }

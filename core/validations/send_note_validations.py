from core.errors.app_exceptions import ValidationError
import re
from decimal import Decimal

def validate_send_note(form_data: dict):
    """
    Valida los campos del formulario de nota.
    Lanza ValidationError si hay algún error.
    Los campos numéricos pueden venir como strings desde el front.
    """

    # Campos obligatorios
    required_fields = [
        ("nombre", "El campo 'Nombre' es obligatorio."),
        ("fecha", "Debe seleccionar una fecha."),
        ("ubicacion", "El campo 'Ubicación' es obligatorio."),
        ("equipo", "El campo 'Equipo' es obligatorio."),
        ("operador", "El campo 'Operador' es obligatorio."),
        ("trabajo_a_realizar", "El campo 'Trabajo a Realizar' es obligatorio."),
        ("firma", "El campo 'Firma Cliente' es obligatorio."),
    ]
    for field, msg in required_fields:
        if not form_data.get(field) or not str(form_data[field]).strip():
            raise ValidationError(msg, field=field)

    # Campos opcionales con límite de caracteres
    optional_max_length = [
        ("empresa", 20, "La empresa no puede superar 20 caracteres."),
        ("ayudante", 20, "El campo 'Ayudante' no puede superar 20 caracteres."),
    ]
    for field, max_len, msg in optional_max_length:
        value = form_data.get(field)
        if value and len(str(value).strip()) > max_len:
            raise ValidationError(msg, field=field)

    # Campos numéricos (pueden venir como string)
    numeric_fields = [
        ("total_horas", "El campo 'Horas de Trabajo' debe ser numérico."),
        ("costo_hora", "El campo 'Costo Hr/Maniobra' debe ser numérico."),
        ("costo_total", "El campo 'Costo Total' debe ser numérico."),
        ("costo_total_iva", "El campo 'Costo Total con IVA' debe ser numérico."),
    ]
    for field, msg in numeric_fields:
        value = form_data.get(field)
        if value is None or str(value).strip() == "":
            continue  # Opcional, si quieres que sea obligatorio quita esta línea
        try:
            Decimal(str(value))
        except Exception:
            raise ValidationError(msg, field=field)

    # Campos de tiempo opcionales (HH:MM)
    time_pattern = re.compile(r"^\d{2}:\d{2}(:\d{2})?$")
    for field in ["salida", "llegada", "termino", "retorno"]:
        value = form_data.get(field)
        if value and not time_pattern.match(str(value)):
            raise ValidationError(f"El campo '{field}' debe tener formato HH:MM.", field=field)

    return True
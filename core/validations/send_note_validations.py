from core.errors.app_exceptions import ValidationError
import re
from decimal import Decimal

def validate_send_note_input(form_data: dict):
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

    # Validar formato de hora
    import re
    time_pattern = re.compile(r"^\d{2}:\d{2}(:\d{2})?$")
    for field in ["salida", "llegada", "termino", "retorno"]:
        value = form_data.get(field)
        if value and not time_pattern.match(str(value)):
            raise ValidationError(f"El campo '{field}' debe tener formato HH:MM.", field=field)

    return True


def validate_send_note(form_data: dict):
    numeric_fields = [
        ("horas_de_trabajo", "El total de horas debe ser numérico."),
        ("costo_hora", "El costo por hora debe ser numérico."),
        ("costo_total", "El costo total debe ser numérico."),
        ("costo_total_con_iva", "El costo total con IVA debe ser numérico."),
    ]
    for field, msg in numeric_fields:
        value = form_data.get(field)
        if value is None:
            raise ValidationError(f"Falta el campo {field}.", field=field)
        try:
            v = float(str(value))
            if v < 0:
                raise ValidationError(f"El campo {field} no puede ser negativo.", field=field)
        except Exception:
            raise ValidationError(msg, field=field)
        
    return True
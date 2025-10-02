from core.errors.app_exceptions import ValidationError

def validate_open_note(data: dict):
    """
    Valida que los campos mínimos de abrir nota sean correctos.
    Lanza ValidationError si algo está mal.
    """
    if not data.get("nombre"):
        raise ValidationError("El nombre es obligatorio.", field="nombre")

    if not data.get("operador"):
        raise ValidationError("El operador es obligatorio.", field="operador")

    if not data.get("fecha"):
        raise ValidationError("La fecha es obligatoria.", field="fecha")
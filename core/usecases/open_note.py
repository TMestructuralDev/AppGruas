from core.gateways.open_notegateway import open_note_gateway
from core.adapters.open_note_adapter import build_open_payload
from core.validations.open_note_validations import validate_open_note
from core.errors.app_exceptions import GatewayError

def open_note(form_data: dict):
    """
    Caso de uso para abrir nota:
    1. Validar datos
    2. Construir payload
    3. Llamar al gateway
    """
    # Validaciones de negocio
    validate_open_note(form_data)

    payload = build_open_payload(form_data)

    try:
        return open_note_gateway(payload)
    except Exception as e:
        # Si el backend da error, lo envolvemos en GatewayError
        raise GatewayError(f"Error al abrir nota en backend: {e}")
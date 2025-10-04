from core.gateways.send_notegateway import send_note_gateway
from core.adapters.send_note_adapter import send_note_payload
from core.validations.send_note_validations import validate_send_note

def send_note(form_data: dict):
    """
    Caso de uso: Enviar nota
    1. Valida datos del formulario
    2. Construye el payload
    3. Llama al gateway
    """
    # Validación de reglas de negocio
    validate_send_note(form_data)

    # Adaptar datos para el backend
    payload = send_note_payload(form_data)

    # Enviar al backend
    return send_note_gateway(payload)
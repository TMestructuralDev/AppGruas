from core.gateways.send_notegateway import send_note_gateway
from core.adapters.send_note_adapter import send_note_payload
from core.validations.send_note_validations import validate_send_note, validate_send_note_input
from core.services.calculate_note_totals import calculate_note_totals

def send_note(form_data: dict):
    """
    Caso de uso: Enviar nota
    1. Valida datos del formulario
    2. Construye el payload
    3. Llama al gateway
    """
    # Validación de datos del formulario previo a calculo
    validate_send_note_input(form_data)
    
    # Llamar a funcion de calculos
    totals = calculate_note_totals(form_data)
    form_data.update(totals)
    
    # Validacion de los datos despues del calculo
    validate_send_note(form_data)
    
    form_data["nota_abierta"] = False
    
    # Adaptar datos para el backend
    payload = send_note_payload(form_data)

    # Enviar al backend
    return send_note_gateway(payload)
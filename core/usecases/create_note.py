from core.gateways.send_note import send_note
from core.adapters.form_adapter import build_payload

def create_note(form_data: dict):
 
    payload = build_payload(form_data)
    return send_note(payload)
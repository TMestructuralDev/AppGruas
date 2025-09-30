from core.gateways.send_notegateway import send_note
from core.adapters.form_adapter import build_payload

def send_note(form_data: dict):
 
    payload = build_payload(form_data)
    return send_note(payload)
from core.gateways.open_notegateway import open_note
from core.adapters.form_adapter import build_open_payload

def open_note(form_data: dict):
    payload = build_open_payload(form_data)
    return open_note(payload)
import requests
from core.adapters.open_note_adapter import build_open_payload

API_URL = "http://127.0.0.1:8000/api/notes/open/"  

def open_note_gateway(form_data: dict):
    """
    Build JSON and send to backend.
    """
    payload = build_open_payload(form_data)
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()
import requests
from core.adapters.form_adapter import build_open_payload

API_URL = "http://127.0.0.1:8000/api/notes/open/"  

def send_open_note(form_data: dict):
    """
    Build JSON and send to backend.
    """
    payload = build_open_payload(form_data)
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()
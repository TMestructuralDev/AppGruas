import requests
from core.adapters.form_adapter import build_payload 

API_URL = "http://127.0.0.1:8000/api/notes/"

def send_note(form_data: dict):
    """
    Construye el JSON usando el adapter y lo envía al backend DRF.
    """
    payload = build_payload(form_data)
    response = requests.post(API_URL, json=payload)
    response.raise_for_status()
    return response.json()
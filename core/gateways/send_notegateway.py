import requests
from core.adapters.send_note_adapter import send_note_payload

API_URL = "http://127.0.0.1:8000/api/notes/"

def send_note_gateway(form_data: dict):
    """
    Construye el JSON usando el adapter y lo envía al backend DRF.
    """
    payload = send_note_payload(form_data)
    print("DEBUG: Payload enviado al backend:", payload)
    
    response = requests.post(API_URL, json=payload)
    print("DEBUG: Status code:", response.status_code)
    print("DEBUG: Response body:", response.text)
    
    response.raise_for_status()
    return response.json()
import requests

API_URL = "http://127.0.0.1:8000/api/notes/"

def send_note_gateway(payload: dict):
    """
    Construye el JSON usando el payload desde el caso de uso
    """
    response = requests.post(API_URL, json=payload)
    print("DEBUG: Status code:", response.status_code)
    print("DEBUG: Response body:", response.text)
    
    response.raise_for_status()
    return response.json()
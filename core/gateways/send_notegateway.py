import requests

API_URL = "http://127.0.0.1:8000/api/notes/"

def send_note_gateway(payload: dict):
    """
    Construye el JSON usando el payload desde el caso de uso
    """
    if not payload.get("id"):
        raise ValueError("El payload debe incluir el 'id' de la nota existente para actualizarla")

    url = f"{API_URL}{payload['id']}/"
    response = requests.put(url, json=payload)
    response.raise_for_status()
    return response.json()
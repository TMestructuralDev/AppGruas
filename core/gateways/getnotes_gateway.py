import requests

class GetNotesGateway:
    def __init__(self, base_url="http://127.0.0.1:8000/api/notes/"):
        self.base_url = base_url

    def fetch_open_notes(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            notes = response.json()
            # Filtramos solo las notas abiertas (nota_abierta=True)
            open_notes = [note for note in notes if note.get("nota_abierta", False)]
            return open_notes
        except requests.exceptions.RequestException as e:
            print(f"Error fetching notes: {e}")
            return []
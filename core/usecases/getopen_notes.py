
from core.gateways.getnotes_gateway import GetNotesGateway
from core.adapters.note_adapter import NoteAdapter

def get_open_notes():
    """
    Usecase para traer notas abiertas.
    """
    notes = GetNotesGateway().fetch_open_notes()
    adapted_notes = NoteAdapter.to_card_list(notes)
    return adapted_notes
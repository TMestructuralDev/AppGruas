from core.gateways.getnotes_gateway import NoteGateway

def get_note_by_id(note_id: int) -> dict:
    """
    Usecase: obtener una nota completa por ID.
    """
    gateway = NoteGateway()
    note = gateway.get_note_by_id(note_id)
    return note
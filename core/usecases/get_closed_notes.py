from core.gateways.getnotes_gateway import GetNotesGateway
from core.adapters.note_card_adapter import NoteAdapter
from core.errors.app_exceptions import GatewayError


def get_closed_notes():
    """
    Caso de uso: Obtener notas cerradas completas (nota_abierta = False).
    """
    try:
        gateway = GetNotesGateway()
        closed_notes = gateway.fetch_closed_notes()
        adapted_notes = NoteAdapter.to_closed_card_list(closed_notes)
        return adapted_notes
    except Exception as e:
        raise GatewayError(f"No se pudieron obtener las notas cerradas: {e}")
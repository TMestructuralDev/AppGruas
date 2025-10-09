from core.gateways.getnotes_gateway import GetNotesGateway
from core.adapters.note_card_adapter import NoteAdapter
from core.errors.app_exceptions import GatewayError


def get_closed_notes():
    """
    Caso de uso: Obtener notas cerradas (nota_abierta = False).
    1. Llama al gateway para traer todas las notas cerradas.
    2. Adapta la respuesta al formato de tarjetas.
    """
    try:
        gateway = GetNotesGateway()
        closed_notes = gateway.fetch_closed_notes()
        adapted_notes = NoteAdapter.to_card_list(closed_notes)
        return adapted_notes
    except Exception as e:
        raise GatewayError(f"No se pudieron obtener las notas cerradas: {e}")
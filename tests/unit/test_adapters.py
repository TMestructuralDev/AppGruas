# tests/unit/test_adapters.py
from datetime import date, time
from core.adapters.send_note_adapter import build_payload, build_open_payload

def test_build_open_payload_converts_fecha():
    form_data = {
        "nombre": "Juan",
        "operador": "Pedro",
        "fecha": date(2025, 9, 30)
    }
    payload = build_open_payload(form_data)
    assert payload["fecha"] == "2025-09-30"
    assert payload["nombre"] == "Juan"
    assert payload["operador"] == "Pedro"

def test_build_payload_converts_tiempos():
    form_data = {
        "nombre": "Juan",
        "fecha": date(2025, 9, 30),
        "salida": time(8, 0),
        "llegada": time(9, 30),
        "termino": time(12, 0),
        "retorno": time(13, 0)
    }
    payload = build_payload(form_data)
    assert payload["fecha"] == "2025-09-30"
    assert payload["salida"] == "08:00"
    assert payload["llegada"] == "09:30"
    assert payload["termino"] == "12:00"
    assert payload["retorno"] == "13:00"

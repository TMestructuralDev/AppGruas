# tests/unit/test_validations.py
import pytest
from core.validations.open_note_validations import validate_open_note
from core.errors.app_exceptions import ValidationError

def test_valid_data_passes():
    form_data = {
        "nombre": "Juan",
        "operador": "Pedro",
        "fecha": "2025-09-30"
    }
    # Solo asegurarnos de que no lanza excepción
    try:
        validate_open_note(form_data)
    except ValidationError:
        pytest.fail("Validación falló con datos correctos")

def test_missing_nombre_raises_error():
    form_data = {
        "nombre": "",
        "operador": "Pedro",
        "fecha": "2025-09-30"
    }
    with pytest.raises(ValidationError) as e:
        validate_open_note(form_data)
    assert "nombre" in str(e.value)

def test_missing_operador_raises_error():
    form_data = {
        "nombre": "Juan",
        "operador": None,
        "fecha": "2025-09-30"
    }
    with pytest.raises(ValidationError) as e:
        validate_open_note(form_data)
    assert "operador" in str(e.value)

def test_missing_fecha_raises_error():
    form_data = {
        "nombre": "Juan",
        "operador": "Pedro",
        "fecha": None
    }
    with pytest.raises(ValidationError) as e:
        validate_open_note(form_data)
    assert "fecha" in str(e.value)

import pytest
from datetime import date, time

@pytest.fixture
def valid_form_data():
    return {
        "nombre": "Juan Pérez",
        "telefono": "1234567890",
        "empresa": "MiEmpresa",
        "fecha": date(2025, 9, 30),
        "ubicacion": "Ciudad",
        "equipo": "Camión",
        "operador": "Pedro",
        "ayudante": None,
        "trabajo_realizar": "Carga de material",
        "salida": time(8, 0),
        "llegada": time(9, 0),
        "termino": time(12, 0),
        "retorno": time(13, 0),
        "total_horas": "5",
        "costo_hora": "100",
        "costo_total": "500",
        "costo_total_iva": "580",
        "firma_cliente": "Firma X",
    }
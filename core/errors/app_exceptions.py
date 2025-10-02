class ValidationError(Exception):
    """Error de validación de reglas de negocio."""
    def __init__(self, message: str, field: str = None):
        self.message = message
        self.field = field
        super().__init__(message)

class GatewayError(Exception):
    """Error al comunicarse con el backend."""
    def __init__(self, message: str, status_code: int = None):
        self.message = message
        self.status_code = status_code
        super().__init__(message)
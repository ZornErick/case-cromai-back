class ValidationErrorResponse:
    """
    Define a estrutura de uma mensagem para erros de validação
    """

    def __init__(self, field, message):
        self.field = field
        self.message = message

    def to_dict(self):
        return {"field": self.field, "message": self.message}


class ErrorResponse:
    """
    Define a estrutura de uma mensagem para erros gerais
    """

    def __init__(self, status, message):
        self.status = status
        self.message = message

    def to_dict(self):
        return {"status": self.status, "message": self.message}

def validar_campos(request_body, campos):
    """
    Valida os campos do corpo da requisição usando como base os campos passados como parâmetro

    :param request_body: corpo da requisição
    :param campos: campos-base para a validação
    :return: campos validados
    """

    campos_validos = dict()
    campos_invalidos = []

    for campo in campos:
        if campo not in request_body.keys():
            campos_invalidos.append(campo)
        else:
            campos_validos[campo] = request_body[campo]

    if len(campos_invalidos) > 1:
        e = NameError()
        e.error = campos_invalidos
        raise e
    elif len(campos_validos) >= 3:
        e = Exception()
        e.error = "informe apenas 2 campos"
        raise e

    return campos_validos


def validar_valores(request_body):
    """
    Valida os valores do corpo da requisição

    :param request_body: corpo da requisição
    :return: void
    """

    value_errors = dict()

    for chave, valor in request_body.items():
        if valor is None:
            value_errors[chave] = "valor deve ser diferente de null"
            break
        if not str(valor).replace(".", "").isnumeric():
            value_errors[chave] = "valor deve ser númerico"
            break
        if float(valor) <= 0:
            value_errors[chave] = "valor deve ser maior que zero"
        if float(valor) > 1000:
            if chave == "cateto_a" or chave == "cateto_b":
                value_errors["cateto"] = "valor deve ser menor que 1000"
            else:
                value_errors["hipotenusa"] = "valor deve ser menor que 1000"

    if len(value_errors) > 0:
        e = ValueError()
        e.error = value_errors
        raise e


def parse_float(request_body):
    """
    Converte os valores de um dicionário para float

    :param request_body: corpo da requisição
    :return: dicionário com valores convertidos para float
    """

    request_body_float = dict()
    for chave, valor in request_body.items():
        request_body_float[chave] = float(valor)

    return request_body_float


def validar(request_body, campos):
    """
    Chama funções de validação

    :param request_body: corpo da requisição
    :param campos: campos-base para a validação
    :return: campos validados e convertidos para float
    """

    campos_validos = validar_campos(request_body, campos)
    validar_valores(campos_validos)

    return parse_float(campos_validos)

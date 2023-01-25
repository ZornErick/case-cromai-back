from flask import jsonify
from validar import validar
from math import sqrt


def calcular_hipotenusa(cateto_a, cateto_b):
    """
    Calcula a hipotenusa a partir dos catetos

    :param cateto_a: comprimento do cateto A
    :param cateto_b: comprimento do cateto B
    :return: comprimento da hipotenusa
    """

    return round(sqrt(cateto_a * cateto_a + cateto_b * cateto_b), 3)


def calcular_cateto(hipotenusa, cateto):
    """
    Calcula um dos catetos a partir da hipotenusa e do cateto

    :param hipotenusa: comprimento da hipotenusa
    :param cateto: comprimento de algum dos catetos
    :return: comprimento do cateto
    """
    if cateto >= hipotenusa:
        e = ValueError()
        e.error = {"cateto": "valor deve ser menor que a hipotenusa"}
        raise e

    return round(sqrt(hipotenusa * hipotenusa - cateto * cateto), 3)


def calcular(request_body):
    """
    Chama uma função par validar o corpo da requisição e define qual cálculo será executado

    :param request_body: corpo da requisição
    :return: função de cálculo
    """

    campos_base = ["hipotenusa", "cateto_a", "cateto_b"]
    data = validar(request_body, campos_base)

    if "hipotenusa" in data.keys():
        cateto = data["cateto_a"] if "cateto_a" in data.keys() else data["cateto_b"]
        return jsonify({"cateto": calcular_cateto(data["hipotenusa"], cateto)})
    else:
        return jsonify({"hipotenusa": calcular_hipotenusa(data["cateto_a"], data["cateto_b"])})

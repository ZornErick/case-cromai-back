from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS

from error_response import ValidationErrorResponse, ErrorResponse
from calcular import calcular

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.errorhandler(Exception)
def handle_exception(error):
    """
    Instancia um objeto da classe ErrorResponse passando para o construtor um HTTP status code e uma mensagem de erro e
    adiciona o objeto a uma lista

    :param error: objeto do tipo Exception
    :return: lista com um dicionário em JSON
    """

    list_errors = [ErrorResponse(400, error.error).to_dict()]
    return jsonify(list_errors), 400


@app.errorhandler(TypeError)
def handle_type_error(error):
    """
    Percorre um dicionário de erros e para cada erro instancia, um objeto do tipo ValidationErrorResponse, adiciona o
    objeto a uma nova lista, passando no construtor a key e o value do dicionário

    :param error: objeto do tipo TypeError
    :return: lista de dicionários em JSON
    """

    list_errors = []
    for key, type_error in error.error.items():
        list_errors.append(ValidationErrorResponse(key, type_error).to_dict())
    return jsonify(list_errors), 400


@app.errorhandler(ValueError)
def handle_value_error(error):
    """
    Percorre um dicionário de erros e para cada erro instancia, um objeto do tipo ValidationErrorResponse, adiciona o
    objeto a uma nova lista, passando no construtor a key e o value do dicionário

    :param error: objeto do tipo ValueError
    :return: lista de dicionários em JSON
    """

    list_errors = []
    for key, value_error in error.error.items():
        list_errors.append(ValidationErrorResponse(key, value_error).to_dict())
    return jsonify(list_errors), 400


@app.errorhandler(NameError)
def handle_name_error(error):
    """
    Percorre uma lista de erros e para cada erro instancia, um objeto do tipo ValidationErrorResponse, adiciona o
    objeto a uma nova lista, passando no construtor o erro e uma mensagem

    :param error: objeto do tipo NameError
    :return: lista de dicionários em JSON
    """

    list_errors = []
    for name_error in error.error:
        list_errors.append(ValidationErrorResponse(name_error, "campo não encontrado").to_dict())
    return jsonify(list_errors), 400


class Calcular(Resource):
    """
    Implementa uma rota para calcular a relação entre os lados de um triângulo retângulo
    """

    def post(self):
        if request.is_json:
            return make_response(calcular(request.get_json()))

        return make_response("Preencha o corpo da requisição em formato json para obter sucesso", 403)


api.add_resource(Calcular, "/calcular")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

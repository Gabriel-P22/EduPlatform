from rest_framework.exceptions import APIException


def ValidationError(APIException):
    status_code = 400
    default_detail = "Parametro invalido para a requisicao"
    default_code = "validation_error"

import json

from core.api_utils import custom_converter


def lambda_handler(event, context):
    {{cookiecutter.serviceLow}}_id = (event.get('pathParameters', {}) or {}).get('{{ cookiecutter.serviceLow }}Id')

    if {{cookiecutter.serviceLow}}_id:
        result = {
            "Hola": f"Mundo for { {{ cookiecutter.serviceLow }}_id }"
        }
    else:
        result = {
            "Hola": "Mundo for all"
        }
    return {
        "statusCode": 200,
        "body": json.dumps(result, default=custom_converter),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }

import json

from core.api_utils import custom_converter


def lambda_handler(event, context):
    {{cookiecutter.serviceLow}}_id = (event.get('pathParameters', {}) or {}).get('{{ cookiecutter.serviceLow }}Id')
    result = {
        "Hola": f"Mundo for { {{cookiecutter.serviceLow}}_id }"
    }
    return {
        "statusCode": 200,
        "body": json.dumps(result, default=custom_converter),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }

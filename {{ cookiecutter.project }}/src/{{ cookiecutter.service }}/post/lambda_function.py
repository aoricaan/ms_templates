import json

from core.api_utils import custom_converter


def lambda_handler(event, context):
    result = {
        "Hola": "Mundo"
    }
    return {
        "statusCode": 200,
        "body": json.dumps(result, default=custom_converter),
        "headers": {"Access-Control-Allow-Origin": "*"}
    }

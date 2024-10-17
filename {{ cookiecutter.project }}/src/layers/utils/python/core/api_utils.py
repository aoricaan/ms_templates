from decimal import Decimal


def custom_converter(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    return str(obj)

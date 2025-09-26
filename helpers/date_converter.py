from datetime import datetime

def date_converter(value):
    if isinstance(value, str):
        return datetime.strptime(value, "%Y-%m-%d").date()
    return value

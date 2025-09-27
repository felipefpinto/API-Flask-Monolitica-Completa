from datetime import datetime

def date_converter(value):
    formatos_aceitos = ["%Y-%m-%d", "%Y/%m/%d", "%d-%m%Y", "%d/%m/%Y"]

    for formato in formatos_aceitos:
        try:
            return datetime.strptime(value, formato).date()
        except ValueError:
            continue
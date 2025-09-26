from datetime import datetime, date
from helpers.date_converter import date_converter

def age_calculator(data_nascimento):
    today = date.today() 
    return today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
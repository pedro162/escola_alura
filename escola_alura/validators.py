import re
from validate_docbr import CPF

def cpf_invalido(val:str)->bool:
    return not CPF().validate(val)

def nome_invalido(nome:str)->bool:
    return not nome.isalpha()

def celular_invalido(celular:str)->bool:
    #86 99999-9999
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model, celular)
    #print(response)
    return not response

import re


def modulo_11_banco(numero):
    numero = re.sub("[^0-9]", "", numero)

    soma = 0
    peso = 2
    base = 9
    contador = len(numero) - 1
    for i in range(contador, -1, -1):
        soma = soma + int(numero[i:i + 1]) * peso
        if peso < base:
            peso += 1
        else:
            peso = 2

    digito = 11 - (soma % 11)
    if digito > 9:
        digito = 0
    # Utilizar o dígito 1(um) sempre que o resultado do cálculo padrão for igual a 0(zero), 1(um) ou 10(dez).
    elif digito == 0:
        digito = 1

    return digito


def modulo_10(numero):
    numero = re.sub("[^0-9]", "", numero)

    soma = 0
    peso = 2
    contador = len(numero) - 1
    while contador >= 0:
        algarismo = int(numero[contador:contador + 1])
        multiplicacao = algarismo * peso

        if multiplicacao > 10:
            multiplicacao = 1 + (multiplicacao - 10)
        elif multiplicacao == 10:
            multiplicacao = 0

        soma += multiplicacao
        if peso == 2:
            peso = 1
        else:
            peso = 2
        contador -= 1

    digito = 10 - (soma % 10)
    if digito == 10:
        digito = 0

    return digito


def barcode_to_linha_digitavel(barcode):
    linha = re.sub("[^0-9]", "", barcode)

    if len(barcode) != 44:
        return ""

    campo1 = linha[0:4] + linha[19:20] + '.' + linha[20:24]
    campo2 = linha[24:29] + '.' + linha[29:34]
    campo3 = linha[34:39] + '.' + linha[39:44]
    campo4 = linha[4:5]
    campo5 = linha[5:19]

    if modulo_11_banco(linha[0:4] + linha[5:44]) != int(campo4):
        return None

    return f"{campo1}{modulo_10(campo1)} {campo2}{modulo_10(campo2)} {campo3}{modulo_10(campo3)} {campo4} {campo5}"

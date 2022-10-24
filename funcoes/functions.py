def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"o resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 101, somar)
exibir_resultado(102, 203, subtrair)
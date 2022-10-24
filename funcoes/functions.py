def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def teste (a, b):
    return a * 4 / 5*3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"o resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 101, somar)
exibir_resultado(102, 203, subtrair)
exibir_resultado(102, 203, teste)

salario  = 1750

def salario_bonus(bonus):
    global  salario
    salario += bonus
    return salario

novoSalario = salario_bonus(520)
print(novoSalario)

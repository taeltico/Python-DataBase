
def somar(a, b):
    return a + b

def multi(a, b):
    return a * b

def exibir_retorno(a, b, funcao):
    resultado = funcao(a, b)
    print(f"o resultado da opracao {a} + {b} = {resultado}")
    return(f"o resultado da opracao {a} + {b} = {resultado}")

def tentativa(multi, exibir_retorno):
    total = multi(exibir_retorno)
    return(f"total é {multi} * {exibir_retorno} = {total}")


print(exibir_retorno(26,15,somar))
print(exibir_retorno(26,15, multi))
print(tentativa(multi,exibir_retorno,tentativa))


def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    print(pos1, pos2, pos_or_kwd, kwd1, kwd2)



print(1, 2, 3, kwd1 = 23, kwd2 = 89)

def criar_carro(modelo, ano, placa,/, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel);

print(criar_carro("palio", "1999", "abc-1234", "fiat", "1.0", "gasolina"));


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







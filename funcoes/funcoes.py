def exibir_mensagem():
    print("Rafael programador")

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}")

def exibir_mensagem_3(nome="anonimo"):
    print(f"seja bem vindo {nome}!")

print(exibir_mensagem())
print(exibir_mensagem_2(nome="Pablo"))
print(exibir_mensagem_2("Rafa"))
print(exibir_mensagem_3())
print(exibir_mensagem_3(nome="NILZA"))

def  calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return sucessor, antecessor

def func():
    print("Rafael Vitor")
    return None

print(calcular_total([23,54,98]))

print(retorna_antecessor_e_sucessor(34))

print(func())

def cursos_programacao (Udemy, Dio, Alura, Dankicode):
    print(f"aulas que eu desejo {Udemy}/{Dio}/{Alura}/{Dankicode}")

print(cursos_programacao("Cybersecurity", "Java", "Python","Pericia forense"))
print(cursos_programacao(Udemy = "Cybersecurity", Dio = "Java", Alura = "Python", Dankicode = "Pericia forense"))
print(cursos_programacao(**{"Udemy": "Cybersecurity", "Dio": "Java", "Alura": "Python", "Dankicode": "Pericia forense"}))

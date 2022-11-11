import email


nome = input("digite seu nome ")
mail = input("digite seu e-mail ")
telefone =int(input("digite seu telefone "))
endereco = input("digite seu endereço ")

print("Olá meu nome é", (nome), "meu numero de telefone é ", (telefone), "meu e-mail é ", (mail), "moro no endereço ", (endereco))


Saldo = 50223
saque = input(" digite o valor ")
valorDisponivel = (Saldo - saque)

print(nome , "seu saldo disponivel é",valorDisponivel)

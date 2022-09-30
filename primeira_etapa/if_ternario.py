saldo = 6000
saque = float(input("insira o valor desejado "))

status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao realizar o saque")
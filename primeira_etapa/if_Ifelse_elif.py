saldo = 2000
saque = float(input("informe o valor "))

if saldo >= saque:
    print ("valor liberado")
if saldo < saque:
    print ("saldo Insuficiente")

idade = 16
consulta = float(input("digite sua idade..."))

if consulta >= idade:
    print ("pode sacar!")
else:
    print("nao pode sacar!")

Opções = int(input("Informe uma opção:[1]Saque\n [2] Extrato \n [3] Investimentos\n [4]Outros:"))

if Opções == 1:
    valor = float(input("Informe o valor que deseja sacar "))

elif Opções == 2:
    print("Exibindo o extrato")

elif Opções == 3:
    print("Abrindo investimentos")

elif Opções == 4:
    print("selecione uma opção")
    Opções = int(input("Informe uma opção:[1]Saque\n [2] Extrato \n [3] Investimentos\n [4]Outros:"))

else:
     sys.exit("opção invalida")


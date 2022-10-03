nome = input("digite eu nome ")

saldo = 1000
Opções = int(input("Informe uma opção:[1]Saque\n [2] Extrato \n [3] Investimentos\n [4]Depositar:"))
saque = (saldo - ("Informe o valor que deseja sacar ")) 

if Opções == 1:
    valor = input("Informe o valor que deseja sacar ")
    
    if saque<=saldo:
        print("saque autorizado", (nome), "Seu saldo disponivel e ", (saldo-saque))
    else:
        print("Ola {name} Seu saldo e insuficiente", "saldo disponivel", (saldo))
    
elif Opções == 2:
    print(saldo)

elif Opções == 3:
    print("Abrindo investimentos")

elif Opções == 4:
    deposito = float(input("digite o valor de deposito")+ saldo)
    print(deposito)

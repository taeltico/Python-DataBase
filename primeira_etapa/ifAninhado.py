conta_normal = True
conta_universitaria = False

saldo = 2000
saque = float(input("insira o valor "))
cheque_especial = 400


if conta_normal:
    if saldo >= saque:
        print( "saque realizado")
    elif saque <=(saldo + cheque_especial):
        print("saque realizado com uso do cheque especial!")
    else:
        print("saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado com sucesso")
    else:
        print("saldo insuficiente")

lista = ["p", "y", "t", "h","o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

veiculos = ["gol", "celta", "civic", "sandeiro", "palio"]

for carro in veiculos:
    print(carro)

for palio in veiculos:
    print(palio)

numeros = [1, 20, 40, 50, 52, 36, 97, 87, 58]
pares =[]

for numero in numeros:
    if numero % 2==0:
        pares.append(numero)


numeros = [1, 20, 40, 50, 52, 36, 97, 87, 58]
pares = [numero for numero in numeros if numero % 2==0]


numeros = [1, 20, 40, 50, 52, 36, 97, 87, 58]
quadrado =[]

for numero in numeros:
    quadrado.append(numero ** 2)
    

numeros = [1, 20, 40, 50, 52, 36, 97, 87, 58]
quadrado =[numero ** 2 for numero in numeros]

bairros = [ "Ipanema", "Copacabana", "cabucu"]
lista.append(1)
lista.append("python")
lista.append([1, 2, 7, 9, 35])

print(bairros)

lista.copy()

print(bairros)

print(lista)


matriz =[
    [ 1, "a", 2]
    [ "b", 3, 4]
    [ 6, 5, "c"]
]
print(matriz[0])
print(matriz[1])
print(matriz[1][1])
print(matriz[-1][-1])
print(matriz[-1][-1])
print(matriz[-1][-1])

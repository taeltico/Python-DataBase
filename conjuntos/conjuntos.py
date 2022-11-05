# SETS

numeros = set([1, 2, 3, 1, 3, 4])

print(numeros)

numeros = set([1, 2, 3, 1, 3, 4])
numeros = list(numeros)
print(numeros[2])



letras = set("abacaxi")

print(letras)

carros = set(("palio", "gol", "celta", "palio"))
for palio in carros:
    print(carros)
print(carros)


conjunto_a ={1, 2}
conjunto_b = {2, 3, 4}

print(conjunto_a.union(conjunto_b))
print(conjunto_a.intersection(conjunto_b))
print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))
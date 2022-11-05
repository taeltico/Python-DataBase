animais = ["vaca", "gato", 123456, 6, 5,52]
numeros = [12, 25, 1, 6, 85, 56, 3, 2, 7,8]

print(animais[0])

animais.remove(52)

print(animais)

print(len(animais))

print("gato" in animais)

animais.append("cobra")

print (animais)

animais.extend(["cachrro", "papagaio", 250, 23])

print(animais)

print(animais.count("gato"))

list.sort(numeros)
print(numeros)

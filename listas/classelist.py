cores = [ "vermelhos", "branco", "blue", "blue", "green"]

cores.count("blue")
cores.count("vermelhos")

numeros = [1, 20, 40, 50, 52, 36, 97, 87, 58]
numeros.count("40")
numeros.count("52")

numeros = [1, 20, 40, 50, 52, 36, 97, 87, 58]
print(numeros.pop())
print(numeros.remove(52))
print(numeros.reverse())
print(numeros.sort())


T = input("digite seu texto...")

if T <= (140):
    print("TWEET")
else:
    print("MUTE")
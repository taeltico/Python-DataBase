curso = "Python"

print(curso.center(10, "#"))
print(".".join(curso))

print(curso.upper())
print(curso.lower())
print(curso.title())
print(curso.upper())

text = "  Hello World!  "

print(text.strip()+ "&")
print(text.rstrip()+ "&")
print(text.lstrip()+ "&")

print(text.center(20, "$"))
print(".".join(curso))

for letra in text:
    print(letra)

nome = "Rafael"
idade = 31
profissão = "Pizzaiolo"
idiomas = "Inglês, Espanhol, Português"

print("Olá, Me chamo %s. eu tenho %d  anos de idade, trabalho como %s e estou aprendendo %s." % (nome, idade, profissão, idiomas))

print("Olá, Me chamo {}. eu tenho {}  anos de idade, trabalho como {} e estou aprendendo {}." .format(nome, idade, profissão, idiomas))

print("Olá, Me chamo {3}. eu tenho {2}  anos de idade, trabalho como {1} e estou aprendendo {0}." .format( idiomas, profissão, idade, nome))

print("Olá, Me chamo {nome}. eu tenho {idade} anos de idade, trabalho como {profissão} e estou aprendendo {idiomas}." .format(nome=nome, idade=idade, profissão=profissão, idiomas=idiomas))

print(f"Olá, Me chamo {nome}. eu tenho {idade} anos de idade, trabalho como {profissão} e estou aprendendo {idiomas}.")

PI = 3.141516

print(f"valor de PI:{PI:.2f}")

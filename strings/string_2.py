nome = "Rafael"
idade = 31
profissão = "Pizzaiolo"
idiomas = "Inglês, Espanhol, Português"

dados = {"nome": "Rafael", "profissão":"Pizzaiolo", "idade":28}


print("nome: %s idade %d" %(nome, idade))
print("nome:{} idade {}".format(nome, idade))
print("nome:{0} trabalho como {2} tenho idade {1}".format(nome, idade, profissão))

print("nome:{nome} trabalho como {profissão} tenho idade {idade}".format(**dados))

print(f"nome:{nome} trabalho como {profissão} tenho idade {idade} estou aprendendo {idiomas}")
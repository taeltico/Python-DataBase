pessoa = {"nome": "rafael", "idade": 31}

pessoa = dict(nome = "rafael", idade = 31)

pessoa[ "telefone"] = "21 96573-8423"

print(pessoa)

dados = { "nome": "Rafael", "idade": 31, "sexo": "Masc", "telefone":"21 96573-8423"}

print(dados["sexo"])

dados["nome"]= input("digite seu nome ")
print(dados["nome"])

contatos ={
    "rafaelanovinha.gr@outlook.com": {"nome": "Rafaela", "idade": 25, "sexo": "Fem", "telefone":"21 96584-2373"},
    "rafaeelo.dz@gmail.com": {"nome": "Rafaelo", "idade": 44, "sexo": "Masc", "telefone":"21 96573-8423"},
    "Rafaellyde@icloud.com": {"nome": "Rafaelly", "idade": 31, "sexo": "Fem", "telefone":"21 97233-8465"}
}

idade = contatos["rafaelanovinha.gr@outlook.com"]["idade"]
print(idade)
cadastros ={
    "rafaelanovinha.gr@outlook.com": {"nome": "Rafaela", "idade": 25, "sexo": "Fem", "telefone":"21 96584-2373"},
    "rafaeelo.dz@gmail.com": {"nome": "Rafaelo", "idade": 44, "sexo": "Masc", "telefone":"21 96573-8423"},
    "Rafaellyde@icloud.com": {"nome": "Rafaelly", "idade": 31, "sexo": "Fem", "telefone":"21 97233-8465"}
}

for chave in cadastros:
    print(chave, cadastros[chave]);

print("Rafaellyde@icloud.com")

for chave, valor in cadastros.items():
    print(chave,valor)
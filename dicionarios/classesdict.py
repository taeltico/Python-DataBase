cadastros ={
    "rafaelanovinha.gr@outlook.com": {"nome": "Rafaela", "idade": 25, "sexo": "Fem", "telefone":"21 96584-2373"},
    "rafaeelo.dz@gmail.com": {"nome": "Rafaelo", "idade": 44, "sexo": "Masc", "telefone":"21 96573-8423"},
    "Rafaellyde@icloud.com": {"nome": "Rafaelly", "idade": 31, "sexo": "Fem", "telefone":"21 97233-8465"}
}

pessoa = {"nome": "rafael", "idade": 31}

pessoa.clear()
print(pessoa, cadastros)

novos = { 
    "joao.dejesus@hotmail.com": {"nome": "Joao", "idade": 29, "sexo": "masc"}
}

copia = novos.copy()

copia["joao.dejesus@hotmail.com"] = {"nome":"Jao", "sexo":"fem"}

print(novos["joao.dejesus@hotmail.com"])

print(copia["joao.dejesus@hotmail.com"])

novos.fromkeys(["tico","teco"])

cadastros.fromkeys(["tico","teco"], "vago")

print(novos)
print(cadastros)


print (cadastros.get("chave"))
print (cadastros.get("chave", {}))
print (cadastros.get("rafaeelo.dz@gmail.com",{}))
print (cadastros.get("joao.dejesus@hotmail.com"))
print (cadastros.get("rafaeelo.dz@gmail.com"))

print(cadastros.keys())

novos.setdefault("bairro", "cabucu")
print(novos)
cadastros.update({"joao.dejesus@hotmail.com": {"nome": "Joao", "idade": 29, "sexo": "masc"}})

print(cadastros)

print(cadastros.values())

cadast = "joao.dejesus@hotmail.com" in novos
print(cadast)

cadast = "sexo" in cadastros["Rafaellyde@icloud.com"]
print(cadast)

del novos["joao.dejesus@hotmail.com"]["sexo"]

print(novos)
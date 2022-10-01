nome = input("digite seu nome ")
idade = input("digite sua idade ")
profissão = input("digite sua profissão")
casa = input("digite seu endereço")
nascimento = input("digite sua data de nascimento")
hobbies = input("o que você gosta de fazer no seu tempo livre?")


mensagem = f"""
Olá! meu nome é {nome}.
Nasci no dia {nascimento},tenho {idade}.
moro em {casa}, Trabalho como {profissão}.
Gosto de {hobbies}.

"""
print(mensagem)
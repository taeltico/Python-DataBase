from xml.dom import DomstringSizeErr


class gato:
    def Normal(Self, nome, cor, cadordado=True):
        Self.nome = nome
        Self.cor = cor
        Self.acordado = Acordado
    
    def miar(Self):
        print("Miau miau")
    
    def dormir(Self):
        Self.acordado = False
        print("zzzzz...")

gato_1 = gato("havenna", "malhada", False)
gato_2 = gato("Pandora", "branca e marrom")

gato_1.miar()

print(gato_2.acordado)
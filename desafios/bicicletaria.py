class Bicicleta ():
    def __init__(self, cor, modelo, ano, valor):
        self.ano = ano
        self.cor = cor
        self.valor = valor
        self.modelo = modelo

    def buzinar(self):
        print("plim plim....")
    
    def parar(self):
        print("parando a bicibleta ...")
        print("bicicleta parada...")
    
    def correr(self):
        print("VRUMMNM...")

b1 = Bicicleta("vernelho", "caloi", 2022, 600)
b2 = Bicicleta("azul", "Shimano", 2010, 1.200)
b3 = Bicicleta("preta e amarela", "poti", 2008, 1.000)
b4 = Bicicleta("Rosa", "seci", 2009, 600)
b5 = Bicicleta("amarela", "Monark", 2008, 1.500)
b6 = Bicicleta("preta ", "Sundow", 2000, 1.000)


b5.buzinar()
b3.correr()
b1.parar()
print(b1.cor, b2.modelo, b5.ano)
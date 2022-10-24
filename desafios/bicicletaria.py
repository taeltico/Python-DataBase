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
        print("biscicleta parada...")
    
    def correr(self):
        print("VRUMMNM...")

b1 = Bicicleta("vernelho", "caloi", 2022, 600)
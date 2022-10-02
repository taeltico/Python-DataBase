entrada = input().split()

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])
resultado = distancia/(diametro1+diametro2)

if (0 < distancia < 10000):
  if(0< diametro1,diametro2< 100):
    print(f'{resultado:.2f}')

# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco Abaixo
ICM = ((diametro2+diametro1)/distancia)

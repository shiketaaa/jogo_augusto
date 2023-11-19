def abrir_arquivo (op):
    return open('pontuacoes.txt',f'{op}')

def SalvarPontos(pontos):
    arq = abrir_arquivo('a')
    arq.write(str(pontos)+"\n")
    arq.close

def GetPontos():
    arquivo = abrir_arquivo('r')
    x = arquivo. readlines()
    numeros = [int(numero) for numero in x]
    numerosordenados = sorted(numeros, reverse= True)
    for i in range (5):
        print (numerosordenados[i])

    arquivo.close
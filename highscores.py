from jogo import pontos
def abrir_arquivo (op):
    return open('pontuacoes.txt',f'{op}')

arq = abrir_arquivo('a')
arq.write(pontos + '\n')
arq.close
arquivo = abrir_arquivo('r')
x = arquivo. readlines()
arquivo.close
y = []
for i in range (0,len(x)):
    y.append(x[i])
y.sort(reverse= True)
print (*y)
# lista = [6,5,7,3,4]
# print (sorted(lista))

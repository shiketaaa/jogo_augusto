import os
import WConio2 as WConio
import cursor
import random
# from __main__ import player

os.system('cls')
cursor.hide()
voce =  [['‗▄█▄‗'],]
obstaculo = '╣▄▄▄╠'

# ©▄█▄©
#  ███
# ©▀█▀©
  #personagem
voceI = 9   #linha
voceJ = 0  #coluna
obstaculoI = 1
obstaculoJ = 0
simbolo = ''
quadros = 500 

contador = 0 #controla a velocidade de movimentos
pontos = 0
while(simbolo != 'o'):
    #posicionar o cursor no começo da tela
    WConio.gotoxy(0,0)
    
    if voceI > 10:
        voceI = 0
    if obstaculoI >9:
        obstaculoI = 0

    velocidade = contador % quadros == 0    
    if velocidade:
        
        #randomiza a posicao de surgimento dos obstaculos
        numero = random.randint(0,3)
        if numero == 0 and obstaculoI == 0:
            obstaculoJ = 0
        elif numero == 1 and obstaculoI == 0:
            obstaculoJ = 3
        elif numero == 2 and obstaculoI == 0:
            obstaculoJ = 6
        elif numero == 3 and obstaculoI == 0:
            obstaculoJ = 9
        pontos += 100
        #mexe obstaculo
        obstaculoI += 1

    print('*' * 24)  #linha de cima
    for i in range(10): #10 linhas
        
        print('▒', end='')  #abre cada linha

        for j in range(12): #23 colunas
           
            if i==voceI and j==voceJ:
                for i in range (len(voce)):
                    print (*voce[i], end= '')
            elif i ==obstaculoI and j == obstaculoJ:
                print (obstaculo, end='')
            else:
                 print(' ', end=' ')
                
            #colisao de personagem e obstaculo
            if obstaculoI == voceI and obstaculoJ == voceJ:
                simbolo = "o"
        
        print('▒')  #fecha cada linha 

    print('*' * 24) #linha de baixo

    # print (player)
    print (f'pontuacao: {pontos}')
    print ("    desvie das barreiras")
    contador += 1
    

    #pegar interações do usuario
    if WConio.kbhit():
        (tecla, simbolo) = WConio.getch()
        
        if simbolo=='a' or simbolo=='A':
            if voceJ>0:
                voceJ -= 3

        elif simbolo=='d' or simbolo=='D':
            if voceJ<9:
                voceJ += 3
        
        #dobra a velocidade uma vez
        if simbolo == ' ':
            quadros = 250
print("Fim do Jogo!")
# os.system('python . ')
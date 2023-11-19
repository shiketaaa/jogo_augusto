import os
import WConio2 as WConio
import cursor
import random
import highscores as hs
# from __main__ import player
def RodarJogo():
    # player = input('digite seu nome:')
    os.system('cls')
    cursor.hide()
    voce =  '‗▄█▄‗'
    obstaculo = '╣▄▄▄╠'
    barreira =  '╣▄▄▄╠'
    cone = '╣▄▄▄╠'

    #personagem
    voceI = 13  #linha
    voceJ = 0  #coluna
    obstaculoI = 1
    obstaculoJ = 0
    barreiraI = 1
    barreiraJ = 0
    coneI = 1
    coneJ = 0
    simbolo = ''
    quadros = 500 

    contador = 0 #controla a velocidade de movimentos
    pontos = 0
    while(simbolo != 'o'):
        #posicionar o cursor no começo da tela
        WConio.gotoxy(0,0)
        
        if obstaculoI >13:
            obstaculoI = 0

        velocidade = contador % quadros == 0    
        if velocidade:
            
            #randomiza a posicao de surgimento dos obstaculos
            numeroobs = random.randint(0,3)
            if numeroobs == 0 and obstaculoI == 1:
                obstaculoJ = 0
            elif numeroobs == 1 and obstaculoI == 1:
                obstaculoJ = 3
            elif numeroobs == 2 and obstaculoI == 1:
                obstaculoJ = 6
            elif numeroobs == 3 and obstaculoI == 1:
                obstaculoJ = 9

            pontos += 100
            #mexe obstaculo
            obstaculoI += 1

            numerobar = random.randint(0,3)
            if numerobar == 0 and obstaculoI == 5:
                barreiraJ = 0
                barreiraI = 0
            elif numerobar == 1 and obstaculoI == 5:
                barreiraJ = 3
                barreiraI = 0
            elif numerobar == 2 and obstaculoI == 5:
                barreiraJ = 6
                barreiraI = 0
            elif numerobar == 3 and obstaculoI == 5:
                barreiraJ = 9
                barreiraI = 0

            barreiraI += 1

            numerocone = random.randint(0,3)
            if numerocone == 0 and barreiraI == 5:
                coneJ = 0
                coneI = 0
            elif numerocone == 1 and barreiraI == 5:
                coneJ = 3
                coneI = 0
            elif numerocone == 2 and barreiraI == 5:
                coneJ = 6
                coneI = 0
            elif numerocone == 3 and barreiraI == 5:
                coneJ = 9
                coneI = 0

            coneI += 1
            

        print('*' * 24)  #linha de cima
        for i in range(14): #10 linhas
            
            print('▒', end='')  #abre cada linha

            for j in range(12): #colunas
            
                if i==voceI and j==voceJ:
                    for i in range (len(voce)):
                        print (f'\033[33m{voce[i]}\033[m', end= '')
                elif i == obstaculoI and j == obstaculoJ:
                    print (f'\033[31m{obstaculo}\033[m', end='')
                elif i ==barreiraI and j == barreiraJ:
                    print (f'\033[32m{barreira}\033[m', end='')
                elif i ==coneI and j == coneJ:
                    print (f'\033[34m{cone}\033[m', end='')
                else:
                    print(' ', end=' ')

                bateubar = barreiraI == voceI and barreiraJ == voceJ 
                bateuobs = obstaculoI == voceI and obstaculoJ == voceJ  
                bateucone = coneI == voceI and coneJ == voceJ
                #colisao de personagem e obstaculo
                if bateuobs or bateubar or bateucone:
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
            if simbolo == ' ' and quadros > 250:
                quadros = 250
                
            #aumenta a velocidade apos dobrar
            if quadros <=250 and quadros >= 70:
                quadros -=10
    print("Fim do Jogo!")
    hs.SalvarPontos(pontos)
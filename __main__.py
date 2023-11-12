import os
from jogo import RodarJogo
from highscores import GetPontos

def Main():
    menu = '1'
    while menu !='3':

        menu = (input("""
        -----MENU-----
        --1 - JOGAR --
        --2 - HIGHSCORES
        --3 - SAIR -----\n"""))


        match menu:

            case '1':
                RodarJogo()


            case '2':
                GetPontos()
            
            case '3':
                print('saiu')
                exit()

            case _:
                print('opcao invalida')

        os.system('pause')
        os.system('cls')

if __name__=="__main__":
    Main()
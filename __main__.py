import os

menu = 1
while menu !=3:

    menu = int(input("""
    -----MENU-----
    --1 - JOGAR --
    --2 - HIGHSCORES
    --3 - SAIR -----\n"""))


    match menu:

        case 1:
            player = input('digite seu nome:')
            os.system ('cls')
            


        case 2:
            arquivo = open('pontuacoes.txt','r')
            print (*arquivo.readlines(25))
            arquivo.close
        
        case 3:
            print('saiu')
            break

        case _:
            print('errado')

    os.system('pause')
    os.system('cls')
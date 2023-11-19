import os
from jogo import RodarJogo
from highscores import GetPontos

class Menu:
    
    def __init__(self):
        self.opcoes = ["Novo Jogo", "High Scores", "Sair"]
        self.linha_grossa = '\u2588' 
        self.linha_fina = '\u2500'  
        self.largura_menu = 50

    def mostrar_menu(self):
        linha_fina = self.linha_fina * self.largura_menu
        linha_grossa = self.linha_grossa * self.largura_menu
        titulo = "Zoroastrēs"
        espacos_laterais = (self.largura_menu - len(titulo)) // 2
        titulo_centralizado = ' ' * espacos_laterais + titulo + ' ' * espacos_laterais

        print(f"\033[34m{linha_grossa}\033[m")  # Linha grossa azul
        print(f"\033[37m{titulo_centralizado}\033[m")  # Texto com a cor branca
        print(f"\033[34m{linha_fina}\033[m")  # Linha fina azul

        for i, opcao in enumerate(self.opcoes, start=1):
            print(f"{i}. {opcao}") 

        print(f"\033[34m{linha_fina}\033[m")  # Linha fina azul
    def sair_do_jogo(self):
        linha_fina = self.linha_fina * self.largura_menu  
        linha_grossa = self.linha_grossa * self.largura_menu
        print("Saindo do jogo. Até a próxima!")
        print(f"\033[34m{linha_grossa}\033[m")  # Linha grossa azul
def Main():
    menu = '1'
    while menu !='3':
        escolha = Menu()
        escolha.mostrar_menu()
        menu = (input("""
        Digite sua escolha:\n"""))


        match menu:

            case '1':
                RodarJogo()


            case '2':
                os.system('cls')
                print ('highscores:')
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
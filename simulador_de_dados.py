# simulador de dado
# simular o usa de um dado, gerando um valor de 1 até 6

import random
import PySimpleGUI as sg


class simuladorDedado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um valor para o dado?'
        #Layout
        self.layout = [[sg.Text('jogar o dado?')],
                       [sg.Button('Sim'), sg.Button('Não')]]

    def iniciar(self):
        #Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #Ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        #Fazer alguma coisa com esses valores

        try:
            if self.eventos == 'Sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Agradecemos sua participação')
            else:
                print('Por favor digite sim ou não')
        except:
            print('Ocorreu um erro ao gerar seu numero')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
    
        
                       


simulador = simuladorDedado()
simulador.iniciar()

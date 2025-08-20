import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_campo(mapa_campo):
    limpar_tela()
    
    for linha in mapa_campo:
        print(''.join(linha))
    
    time.sleep(0.2)

def campo_marcado(mapa_campo, inicio):
    mapa_trabalho = [linha[:] for linha in mapa_campo]
    
    linhas = len(mapa_trabalho)
    colunas = len(mapa_trabalho[0])
    
    y_inicial, x_inicial = inicio
    mapa_trabalho[y_inicial][x_inicial] = 'O'
    imprimir_campo(mapa_trabalho)
    
    for linha in range(1, linhas-1):
        if linha % 2 == 1:
            inicio, fim, passo = 1, colunas-1, 1
        else:
            inicio, fim, passo = colunas-2, 0, -1
        
        for coluna in range(inicio, fim, passo):
            if mapa_trabalho[linha][coluna] == '#':
                continue
            
            mapa_trabalho[linha][coluna] = 'O'
            imprimir_campo(mapa_trabalho)
            
            mapa_trabalho[linha][coluna] = '*'
    
    mapa_trabalho[y_inicial][x_inicial] = 'O'
    imprimir_campo(mapa_trabalho)
    
    print("Sementes soltas!")

def Soltar():
    # Mapa do campo 10 x 10
    mapa_campo = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
    
    # Posição inicial do robô (linha, coluna)
    inicio = (1, 1)
    
    print("Simulador de Robô Solta_Semente")
    print("Legenda:")
    print("  # - Limites")
    print("  O - Robô")
    print("  * - Área plantada")
    print("  ' ' - Área vazia")
    input("\nPressione Enter para iniciar...")
    
    campo_marcado(mapa_campo, inicio)
    
    input("\nPressione Enter para sair...")

Soltar()
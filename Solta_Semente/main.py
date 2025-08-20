import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_campo(mapa_campo):
    limpar_tela()
    
    for linha in mapa_campo:
        print(''.join(linha))
    
    time.sleep(0.2)

def campo_marcado(mapa_campo, posicao_inicial):
    # Cria uma cópia do mapa para trabalhar
    mapa_trabalho = [linha[:] for linha in mapa_campo]
    
    # Obtém as dimensões do mapa
    linhas = len(mapa_trabalho)
    colunas = len(mapa_trabalho[0])
    
    # Marca a posição inicial
    y_inicial, x_inicial = posicao_inicial
    mapa_trabalho[y_inicial][x_inicial] = 'O'
    imprimir_campo(mapa_trabalho)
    
    # Para cada linha do mapa (de cima para baixo)
    for linha in range(1, linhas-1):
        # Decide a direção da varredura baseada na paridade da linha
        if linha % 2 == 1:  # Linhas ímpares: esquerda para direita
            inicio, fim, passo = 1, colunas-1, 1
        else:  # Linhas pares: direita para esquerda
            inicio, fim, passo = colunas-2, 0, -1
        
        # Para cada coluna na direção atual
        for coluna in range(inicio, fim, passo):
            # Se a célula atual for uma parede, pule
            if mapa_trabalho[linha][coluna] == '#':
                continue
            
            # Move o robô para a nova posição
            mapa_trabalho[linha][coluna] = 'O'
            imprimir_campo(mapa_trabalho)
            
            # Marca a posição com semente
            mapa_trabalho[linha][coluna] = '*'
    
    # Retorna para a posição inicial
    mapa_trabalho[y_inicial][x_inicial] = 'O'
    imprimir_campo(mapa_trabalho)
    
    print("Sementes soltas!")

def Soltar():
    # Mapa da sala 10x10 com obstáculos
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
    posicao_inicial = (1, 1)
    
    print("Simulador de Robô Solta_Semente")
    print("Legenda:")
    print("  # - Limites")
    print("  O - Robô")
    print("  * - Área plantada")
    print("  ' ' - Área vazia")
    input("\nPressione Enter para iniciar...")
    
    # Inicia a plantação
    campo_marcado(mapa_campo, posicao_inicial)
    
    input("\nPressione Enter para sair...")

Soltar()
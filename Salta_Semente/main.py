import os
import time

def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_sala(mapa_sala):
    """Imprime o mapa da sala no console"""
    limpar_tela()
    
    for linha in mapa_sala:
        print(''.join(linha))
    
    time.sleep(0.2)

def limpar_sala(mapa_sala, posicao_inicial):
    """
    Faz o robô limpar toda a sala em padrão simples da esquerda para a direita
    """
    # Cria uma cópia do mapa para trabalhar
    mapa_trabalho = [linha[:] for linha in mapa_sala]
    
    # Obtém as dimensões do mapa
    linhas = len(mapa_trabalho)
    colunas = len(mapa_trabalho[0])
    
    # Marca a posição inicial
    y_inicial, x_inicial = posicao_inicial
    mapa_trabalho[y_inicial][x_inicial] = 'O'
    imprimir_sala(mapa_trabalho)
    
    # Para cada linha do mapa (de cima para baixo)
    for linha in range(1, linhas-1):
        # Decide a direção da varredura (da esquerda para a direita)
        inicio, fim, passo = 1, colunas-1, 1
        
        # Para cada coluna na direção atual
        for coluna in range(inicio, fim, passo):
            # Se a célula atual for uma parede, pule
            if mapa_trabalho[linha][coluna] == '#':
                continue
            
            # Move o robô para a nova posição
            mapa_trabalho[linha][coluna] = 'O'
            imprimir_sala(mapa_trabalho)
            
            # Marca a posição como limpa
            mapa_trabalho[linha][coluna] = '*'
    
    # Retorna para a posição inicial
    mapa_trabalho[y_inicial][x_inicial] = 'O'
    imprimir_sala(mapa_trabalho)
    
    print("Limpeza concluída!")

def main():
    # Mapa da sala 10x10 com obstáculos
    mapa_sala = [
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
    
    print("Simulador de Robô Aspirador")
    print("Legenda:")
    print("  # - Parede/obstáculo")
    print("  O - Robô")
    print("  * - Área limpa")
    print("  ' ' - Área suja")
    input("\nPressione Enter para iniciar...")
    
    # Inicia a limpeza
    limpar_sala(mapa_sala, posicao_inicial)
    
    input("\nPressione Enter para sair...")

if __name__ == "__main__":
    main()
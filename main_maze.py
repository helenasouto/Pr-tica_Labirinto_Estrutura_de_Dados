# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque

def solve_maze_backtracking(maze):
    """
    Resolve o labirinto usando backtracking e uma pilha.
    """
    
    # Cria uma nova pilha para o backtracking
    s = deque()
    
    # Localiza a posição inicial do jogador e a insere na pilha
    initial_pos = maze.get_init_pos_player()
    s.append(initial_pos)
    
    # Conjunto para armazenar posições visitadas e evitar loops
    visited = set()
    visited.add(initial_pos)
    
    # Enquanto a pilha não estiver vazia
    while s:
        # Retira uma localização (linha, coluna) da pilha
        current_pos = s.pop()
        
        # Move o jogador para a posição atual para visualização
        maze.mov_player(current_pos)
        time.sleep(0.1)  # Atraso para visualização
        
        # Se a posição tiver o prêmio, o caminho foi encontrado
        if maze.find_prize(current_pos):
            print("Caminho encontrado!")
            return True
            
        # Examina as casas adjacentes (cima, baixo, esquerda, direita)
        x, y = current_pos
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        
        for neighbor in neighbors:
            # Se a casa adjacente estiver livre e não tiver sido visitada
            if maze.is_free(neighbor) and neighbor not in visited:
                # Insere a posição na pilha e marca como visitada
                s.append(neighbor)
                visited.add(neighbor)
                
    # Se a pilha esvaziar e o prêmio não for encontrado
    print("Caminho não encontrado.")
    return False

# Inicializa o labirinto
maze_csv_path = "labirinto1.txt"
maze = Maze()
maze.load_from_csv(maze_csv_path)

# Exibe o labirinto e inicializa o jogador e o prêmio
maze.run()
maze.init_player()

# Resolve o labirinto usando o algoritmo de backtracking
solve_maze_backtracking(maze)

# Mantém a janela do Pygame aberta após a resolução
while True:
    pass
import os 
import random

def gerar_arquivo(num_vertices):
    peso_min=1
    peso_max=50
    """
    Gera um arquivo de grafo no formato especificado.
    
    Args:
        nome_arquivo (str): Nome do arquivo para salvar
        num_vertices (int): Número de vértices do grafo
        peso_min (int): Peso mínimo das arestas
        peso_max (int): Peso máximo das arestas
    """
    # Cria matriz de adjacência
    matriz = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    
    # Preenche a matriz com pesos aleatórios (grafo completo)
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            peso = random.randint(peso_min, peso_max)
            matriz[i][j] = peso
            matriz[j][i] = peso  # Grafo não-direcionado
    
    # Salva no arquivo
    with open('arquivo_exemplo', 'w') as arquivo:
        # Escreve o número de vértices
        arquivo.write(f"{num_vertices}\n")
        
        # Escreve a matriz de adjacência
        for linha in matriz:
            linha_str = ' '.join(str(peso) for peso in linha)
            arquivo.write(linha_str + '\n')
    

def ler_matriz_de_arquivo(caminho_arquivo):

    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Lê o tamanho (número de vértices)
    tamanho = int(linhas[0].strip())
    
    # Lê a matriz de adjacência
    matriz = []
    for i in range(1, tamanho + 1):
        linha = list(map(int, linhas[i].strip().split()))
        matriz.append(linha)
    
    return tamanho, matriz



def exibir_matriz(matriz, tamanho):
    """
    Exibe a matriz de adjacência formatada.
    
    Args:
        matriz: Matriz de adjacência
        tamanho: Número de vértices
    """
    print(f"\n=== MATRIZ DE ADJACÊNCIA ({tamanho}x{tamanho}) ===")
    
    # Cabeçalho com índices das colunas
    print("   ", end="")
    for j in range(tamanho):
        print(f"{j:4d}", end="")
    print()
    
    # Linhas da matriz
    for i in range(tamanho):
        print(f"{i:2d} ", end="")
        for j in range(tamanho):
            print(f"{matriz[i][j]:4d}", end="")
        print()
    
    print("=" * (tamanho * 4 + 3))
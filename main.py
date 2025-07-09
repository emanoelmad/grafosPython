#!/usr/bin/env python3
from grafosPython import geradorArquivo
from grafosPython import algoritmos
import os 
def main():
    """
    Função principal do programa.
    """
    # print("=== Gerador de Grafos ===")
    # print("Este é um gerador de grafos simples.")
    # num_vertices = int(input("Digite o número de vértices do grafo: "))
    # geradorArquivo.gerar_arquivo(num_vertices)

    # Busca o arquivo gerado e lê a matriz
    caminho_arquivo = "arquivo_exemplo"
    tamanho, matriz = geradorArquivo.ler_matriz_de_arquivo(caminho_arquivo)
    geradorArquivo.exibir_matriz(matriz,tamanho)
    arestas_agm, peso_total = algoritmos.kuskralAlgoritmo.kruskal(matriz, tamanho)

if __name__ == "__main__":
    main()
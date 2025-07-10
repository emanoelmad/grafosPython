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
    
    arestas_agm, peso_total, matrizDesigualdadeResolvida= algoritmos.kuskralAlgoritmo.kruskal(matriz, tamanho)
    impares = algoritmos.vertices_grau_impar(arestas_agm, tamanho)
    print("vertices de grau ímpar:", impares)
    matching = algoritmos.emparelhamento_perfeito_minimo(matrizDesigualdadeResolvida, impares)
    print("Emparelhamento perfeito mínimo:", matching)

    arestas_multigrafo = algoritmos.unir_agm_emparelhamento(arestas_agm, matching, matrizDesigualdadeResolvida)
    print("Arestas do multigrafo (AGM + emparelhamento):")
    for origem, destino, peso in arestas_multigrafo:
        print(f"{origem} -- {destino} (peso: {peso})")

    cicloEuleriano = algoritmos.ciclo_euleriano(arestas_multigrafo)
    print("Ciclo euleriano:", cicloEuleriano)
    cicloHamiltoniano = algoritmos.ciclo_hamiltoniano_de_euleriano(cicloEuleriano)
    print("Ciclo hamiltoniano:", cicloHamiltoniano)

if __name__ == "__main__":
    main()
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

    # Passo 1: Verificando desigualdade triangular e gerando AGM
    print("=" * 30)
    print ("Passo 1: Verificando desigualdade triangular e gerando AGM")
    arestas_agm, matrizDesigualdadeResolvida = algoritmos.prim(matriz, tamanho)
    if arestas_agm == []:
        print("Não foi possível gerar a Árvore Geradora Mínima devido à desigualdade triangular.")
        return
    
    # Passo 2: Verificando vértices de grau ímpar
    impares = algoritmos.vertices_grau_impar(arestas_agm, tamanho)
    print("=" * 30)
    print("Passo 2: Verificando vértices de grau ímpar")
    print("vertices de grau ímpar:", impares)
    print("=" * 30)

    # Passo 3: Emparelhamento perfeito mínimo
    print("Passo 3: Emparelhamento perfeito mínimo")
    matching = algoritmos.emparelhamento_perfeito_minimo(matrizDesigualdadeResolvida, impares)
    print("Emparelhamento perfeito mínimo:", matching)
    print("=" * 30)

    # Passo 4: Unindo AGM e emparelhamento para formar o multigrafo
    print("Passo 4: Unindo AGM e emparelhamento para formar o multigrafo")
    arestas_multigrafo = algoritmos.unir_agm_emparelhamento(arestas_agm, matching, matrizDesigualdadeResolvida)
    print("Arestas do multigrafo (AGM + emparelhamento):")
    peso_total_multigrafo = 0
    for origem, destino, peso in arestas_multigrafo:
        peso_total_multigrafo += peso
        print(f"{origem} -- {destino} (peso: {peso})")
    print(f"Peso total do multigrafo: {peso_total_multigrafo}")
    print("=" * 30)

    # Passo 5: Encontrando o ciclo euleriano
    print("Passo 5: Encontrando o ciclo euleriano")
    cicloEuleriano = algoritmos.ciclo_euleriano(arestas_multigrafo)
    print("Ciclo euleriano:", cicloEuleriano)
    peso_ciclo_euleriano = algoritmos.calcular_peso_ciclo(cicloEuleriano, matrizDesigualdadeResolvida)
    print(f"Peso do ciclo euleriano: {peso_ciclo_euleriano}")

    print("=" * 30)
    # Passo 6: Transformando o ciclo euleriano em ciclo hamiltoniano
    print("Passo 6: Transformando o ciclo euleriano em ciclo hamiltoniano")
    cicloHamiltoniano = algoritmos.ciclo_hamiltoniano_de_euleriano(cicloEuleriano)
    print("Ciclo hamiltoniano:", cicloHamiltoniano)
    peso_ciclo_hamiltoniano = algoritmos.calcular_peso_ciclo(cicloHamiltoniano, matrizDesigualdadeResolvida)
    print(f"Peso do ciclo hamiltoniano: {peso_ciclo_hamiltoniano}")
    print("=" * 30)

if __name__ == "__main__":
    main()
from grafosPython import geradorArquivo
import networkx as nx

def calcular_peso_ciclo(ciclo, matriz):
    """
    Calcula o peso total de um ciclo baseado na matriz de adjacência.
    
    Args:
        ciclo: Lista de vértices representando o ciclo
        matriz: Matriz de adjacência com os pesos das arestas
    
    Returns:
        int: Peso total do ciclo
    """
    peso_total = 0
    for i in range(len(ciclo) - 1):
        origem = ciclo[i]
        destino = ciclo[i + 1]
        peso_total += matriz[origem][destino]
    return peso_total

def exibir_agm(arestas_agm, peso_total, tamanho):

        print("=" * 50)
        print("ÁRVORE GERADORA MÍNIMA")
        print("=" * 50)
        
        if not arestas_agm:
            print("Nenhuma árvore geradora mínima encontrada!")
            return
        
        print(f"Número de vértices: {tamanho}")
        print(f"Número de arestas na AGM: {len(arestas_agm)}")
        print(f"Peso total da AGM: {peso_total}")
        print("\nArestas da AGM:")
        print("-" * 30)
        
        for i, (origem, destino, peso) in enumerate(arestas_agm, 1):
            print(f"{i:2d}. Vértice {origem} -- Vértice {destino} (peso: {peso})")
        
def verifica_desigualdade_triangular(matriz):
    n = len(matriz)
    violacoes = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == i or k == j:
                    continue
                if matriz[i][j] > matriz[i][k] + matriz[k][j]:
                    violacoes += 1
    if violacoes == 0:
        return True
    else:
        print(f"Total de violações encontradas: {violacoes}")
        return False


# Passo 1 Algoritmo de Prim 
# Verifica se a matriz de adjacência satisfaz a desigualdade triangular
def prim(matriz, tamanho):

    if not verifica_desigualdade_triangular(matriz):        
        print("\nDesigualdade triangular detectada")
        return [], matriz
    """
    Algoritmo de Prim para encontrar a Árvore Geradora Mínima.
    """
    # Inicialização
    visitados = [False] * tamanho
    custos = [float('inf')] * tamanho
    pais = [-1] * tamanho
    
    # Começa do vértice 0
    custos[0] = 0
    arestas_agm = []
    peso_total = 0
    
    for _ in range(tamanho):
        # Encontra o vértice de menor custo não visitado
        u = -1
        for v in range(tamanho):
            if not visitados[v] and (u == -1 or custos[v] < custos[u]):
                u = v
        
        visitados[u] = True
        
        # Adiciona aresta à AGM (exceto a primeira)
        if pais[u] != -1:
            arestas_agm.append((pais[u], u, matriz[pais[u]][u]))
            peso_total += matriz[pais[u]][u]
        
        # Atualiza custos dos vizinhos
        for v in range(tamanho):
            if not visitados[v] and matriz[u][v] < custos[v]:
                custos[v] = matriz[u][v]
                pais[v] = u
    exibir_agm(arestas_agm, peso_total, tamanho)

    return arestas_agm, matriz

# Passo 2 Verifica os vértices de grau ímpar
def vertices_grau_impar(arestas_agm, tamanho):
    """
    Retorna uma lista com os vértices de grau ímpar na AGM.
    Args:
        arestas_agm: lista de arestas da AGM no formato (origem, destino, peso)
        tamanho: número de vértices do grafo
    Returns:
        List[int]: vértices de grau ímpar
    """
    graus = [0] * tamanho
    for origem, destino, _ in arestas_agm:
        graus[origem] += 1
        graus[destino] += 1
    return [v for v in range(tamanho) if graus[v] % 2 == 1]

 # Passo 3 Emparelhamento Perfeito Mínimo   
def emparelhamento_perfeito_minimo(matriz, vertices_impares):

    G = nx.Graph()
    for i in vertices_impares:
        for j in vertices_impares:
            if i < j:
                G.add_edge(i, j, weight=matriz[i][j])
    matching = nx.algorithms.matching.min_weight_matching(G)
    
    peso_matching = sum(matriz[u][v] for u, v in matching)
    print("Peso total do emparelhamento:", peso_matching)
    return matching

# Passo 4 Unir AGM e Emparelhamento
def unir_agm_emparelhamento(arestas_agm, matching, matriz):
    """
    Retorna a lista de arestas do multigrafo H (AGM + emparelhamento perfeito mínimo).
    """
    arestas_multigrafo = arestas_agm.copy()
    for u, v in matching:
        peso = matriz[u][v] if u < v else matriz[v][u]
        arestas_multigrafo.append((u, v, peso))
    return arestas_multigrafo

# Passo 5 Ciclo Euleriano
def ciclo_euleriano(arestas_multigrafo):
    """
    Encontra um ciclo euleriano em um multigrafo usando o algoritmo de Hierholzer.
    
    Args:
        arestas_multigrafo: lista de arestas (u, v, peso)
    
    Returns:
        List[int]: Lista de vértices na ordem do ciclo euleriano
    """
    # Constrói lista de adjacência com contagem de arestas (multigrafo)
    adj = {}
    for u, v, _ in arestas_multigrafo:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append(v)
        adj[v].append(u)

    # Copia para manipulação
    adj_copy = {k: adj[k][:] for k in adj}

    # Começa de qualquer vértice
    stack = [next(iter(adj))]
    caminho = []

    # Algoritmo de Hierholzer
    while stack:
        v = stack[-1]
        if adj_copy[v]:
            u = adj_copy[v].pop()
            adj_copy[u].remove(v)
            stack.append(u)
        else:
            caminho.append(stack.pop())

    # Reverte o caminho para obter a ordem correta
    caminho.reverse()
    return caminho

# Passo 6 Ciclo Hamiltoniano de Euleriano
def ciclo_hamiltoniano_de_euleriano(ciclo_euleriano):
    """
    Realiza o shortcutting no ciclo euleriano para obter um ciclo hamiltoniano,
    preservando a ordem original do ciclo euleriano.
    
    Args:
        ciclo_euleriano: lista de vértices do ciclo euleriano
    
    Returns:
        List[int]: Lista de vértices do ciclo hamiltoniano
    """
    visitados = set()  # Conjunto para armazenar vértices já visitados
    ciclo_hamiltoniano = []  # Lista para armazenar o ciclo hamiltoniano

    for vertice in ciclo_euleriano:
        if vertice not in visitados:
            ciclo_hamiltoniano.append(vertice)
            visitados.add(vertice)

    # Fecha o ciclo hamiltoniano retornando ao vértice inicial
    if ciclo_hamiltoniano and ciclo_hamiltoniano[0] != ciclo_hamiltoniano[-1]:
        ciclo_hamiltoniano.append(ciclo_hamiltoniano[0])

    return ciclo_hamiltoniano
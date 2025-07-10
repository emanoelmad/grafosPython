from grafosPython import geradorArquivo
import networkx as nx


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

class UnionFind:
    """
    Estrutura de dados Union-Find (Disjoint Set) para o algoritmo de Kruskal.
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """
        Encontra o representante do conjunto que contém x.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Compressão de caminho
        return self.parent[x]
    
    def union(self, x, y):
        """
        Une os conjuntos que contêm x e y.
        """
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Já estão no mesmo conjunto
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

#passo 2 Algoritmo de Kuskral
class kuskralAlgoritmo:   
    
    def kruskal(matriz, tamanho):
        if not kuskralAlgoritmo.verifica_desigualdade_triangular(matriz):
            matriz = kuskralAlgoritmo.corrigir_desigualdade_triangular(matriz)
            print("\nDesigualdade triangular detectada e corrigida.")
            geradorArquivo.exibir_matriz(matriz,tamanho)


        
        # Extrai todas as arestas da matriz
        arestas = []
        for i in range(tamanho):
            for j in range(i + 1, tamanho):  # Evita duplicatas (grafo não-direcionado)
                if matriz[i][j] > 0:
                    arestas.append((matriz[i][j], i, j))  # (peso, origem, destino)
        
        # Ordena as arestas por peso (crescente)
        arestas.sort()
        
        # Inicializa Union-Find
        uf = UnionFind(tamanho)
        
        # Lista para armazenar as arestas da AGM
        arestas_agm = []
        peso_total = 0
        
        # Processa as arestas em ordem crescente de peso
        for peso, origem, destino in arestas:
            # Se os vértices não estão no mesmo conjunto (não forma ciclo)
            if uf.union(origem, destino):
                arestas_agm.append((origem, destino, peso))
                peso_total += peso
                
                # Se já temos (n-1) arestas, paramos
                if len(arestas_agm) == tamanho - 1:
                    break
        
        kuskralAlgoritmo.exibir_agm(arestas_agm, peso_total, tamanho)

        return arestas_agm, peso_total, matriz
    
    def exibir_agm(arestas_agm, peso_total, tamanho):

        """
        Exibe a Árvore Geradora Mínima de forma organizada.
        
        Args:
            arestas_agm: Lista de arestas da AGM no formato (origem, destino, peso)
            peso_total: Peso total da AGM
            tamanho: Número de vértices do grafo
        """
        print("=" * 50)
        print("ÁRVORE GERADORA MÍNIMA (Algoritmo de Kruskal)")
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
        
        print("-" * 30)
        print(f"PESO TOTAL: {peso_total}")
        print("=" * 50)

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

    def corrigir_desigualdade_triangular(matriz):

        n = len(matriz)
        # Cria uma cópia da matriz para não alterar a original
        dist = [linha[:] for linha in matriz]
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist


 # Passo 3 Emparelhamento Perfeito Mínimo   
def emparelhamento_perfeito_minimo(matriz, vertices_impares):



    """
    Retorna o emparelhamento perfeito mínimo no subgrafo induzido pelos vértices ímpares.
    Args:
        matriz: matriz de adjacência do grafo original
        vertices_impares: lista de vértices de grau ímpar
    Returns:
        set de arestas do emparelhamento (tuplas (u, v))
    """
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

    # Começa do vértice 0 se existir
    vertices_disponiveis = list(adj.keys())
    vertice_inicial = 0 if 0 in vertices_disponiveis else vertices_disponiveis[0]
    stack = [vertice_inicial]
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
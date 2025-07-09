from grafosPython import geradorArquivo


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

class kuskralAlgoritmo:   
    
    def kruskal(matriz, tamanho):
        if not kuskralAlgoritmo.verifica_desigualdade_triangular(matriz):
            xd = kuskralAlgoritmo.corrigir_desigualdade_triangular(matriz)
            print("\nDesigualdade triangular detectada e corrigida.")
            geradorArquivo.exibir_matriz(xd,tamanho)


        
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
        return arestas_agm, peso_total
    
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
                        print(f"Violação: c({i},{j}) = {matriz[i][j]} > c({i},{k}) + c({k},{j}) = {matriz[i][k]} + {matriz[k][j]}")
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
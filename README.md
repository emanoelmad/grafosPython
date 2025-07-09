# Trabalho Final - Algoritmos em Grafos (UFC - Christofides TSP)

Este projeto implementa uma solução aproximada para o Problema do Caixeiro Viajante Métrico (Δ-TSP) usando o Algoritmo de Christofides, conforme especificado na disciplina de Algoritmos em Grafos da UFC - Campus de Crateús.

## Estrutura dos Arquivos

- `main.py`: Arquivo principal para execução do algoritmo.
- `grafosPython/algoritmos.py`: Implementação dos principais algoritmos (Kruskal, emparelhamento, etc).
- `grafosPython/geradorArquivo.py`: Funções auxiliares para leitura e exibição de matrizes.
- `arquivo_exemplo`: Exemplo de arquivo de entrada (matriz de adjacência).

## Requisitos

- Python 3.8+
- [NetworkX](https://networkx.org/) (para emparelhamento perfeito mínimo)

Instale as dependências com:
```sh
pip install networkx
```

## Como preparar o arquivo de entrada

O arquivo de entrada deve ser um arquivo `.txt` (ex: `arquivo_exemplo`) com o seguinte formato:

```
N
a11 a12 a13 ... a1N
a21 a22 a23 ... a2N
...
aN1 aN2 aN3 ... aNN
```
Onde `N` é o número de vértices e cada linha seguinte representa uma linha da matriz de adjacência.

**Exemplo:**
```
5
0 2 9 10 7
2 0 6 4 3
9 6 0 8 5
10 4 8 0 1
7 3 5 1 0
```

## Como executar

1. Certifique-se de que o arquivo de entrada (`arquivo_exemplo`) está na mesma pasta do projeto ou ajuste o caminho no `main.py`.
2. Execute o programa principal:

```sh
python main.py
```

## O que o programa faz

- Lê a matriz de adjacência do arquivo.
- Corrige a matriz para garantir a desigualdade triangular, se necessário.
- Calcula a Árvore Geradora Mínima (AGM) com Kruskal.
- Identifica os vértices de grau ímpar na AGM.
- Calcula o emparelhamento perfeito mínimo entre os vértices ímpares.
- Une as arestas da AGM e do emparelhamento para formar o multigrafo.
- (Próximos passos: ciclo euleriano e ciclo hamiltoniano, se implementados.)

## Saída

O programa exibe no terminal:
- A matriz de adjacência (original e corrigida, se necessário)
- A AGM e seu peso total
- Os vértices de grau ímpar
- O emparelhamento perfeito mínimo e seu peso
- As arestas do multigrafo (AGM + emparelhamento)

---

**Dúvidas ou problemas?**  
Entre em contato com o(s) autor(es) ou consulte o professor da disciplina.
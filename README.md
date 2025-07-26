
# Projeto: Algoritmos em Grafos - Solução Aproximada para o Caixeiro Viajante (Christofides TSP)

Este projeto resolve o Problema do Caixeiro Viajante Métrico (Δ-TSP) utilizando o Algoritmo de Christofides, abordando conceitos de AGM, emparelhamento perfeito mínimo, ciclo euleriano e ciclo hamiltoniano.

## Estrutura do Projeto

- `main.py`: Executa o fluxo principal do algoritmo.
- `grafosPython/algoritmos.py`: Algoritmos de grafos (Prim, emparelhamento, ciclo euleriano/hamiltoniano, etc).
- `grafosPython/geradorArquivo.py`: Funções para leitura, geração e exibição de matrizes.
- `arquivo_exemplo`: Exemplo de matriz de adjacência para testes.

## Requisitos

- Python 3.8 ou superior
- [NetworkX](https://networkx.org/) (usado para emparelhamento perfeito mínimo)

Instale as dependências com:
```sh
pip install networkx
```

## Passos para Executar o Projeto

1. **Prepare o arquivo de entrada**
   - Crie um arquivo de texto (ex: `arquivo_exemplo`) com o seguinte formato:
     ```
     N
     a11 a12 a13 ... a1N
     a21 a22 a23 ... a2N
     ...
     aN1 aN2 aN3 ... aNN
     ```
     Onde `N` é o número de vértices e cada linha representa uma linha da matriz de adjacência.
   - Exemplo:
     ```
     5
     0 2 9 10 7
     2 0 6 4 3
     9 6 0 8 5
     10 4 8 0 1
     7 3 5 1 0
     ```

2. **Execute o programa**
   - Certifique-se de que o arquivo de entrada está na mesma pasta do projeto ou ajuste o caminho no `main.py`.
   - Execute o comando:
     ```sh
     python main.py
     ```

## Funcionamento do Algoritmo

O programa realiza os seguintes passos:

1. **Leitura da matriz de adjacência**
   - Lê o arquivo de entrada e exibe a matriz.
2. **Verificação da desigualdade triangular**
   - Corrige a matriz, se necessário, para garantir que satisfaça a desigualdade triangular.
3. **Geração da Árvore Geradora Mínima (AGM)**
   - Utiliza o algoritmo de Prim para gerar a AGM e calcula seu peso.
4. **Identificação dos vértices de grau ímpar**
   - Encontra os vértices de grau ímpar na AGM.
5. **Emparelhamento perfeito mínimo**
   - Calcula o emparelhamento perfeito mínimo entre os vértices ímpares usando NetworkX.
6. **Formação do multigrafo**
   - Une as arestas da AGM e do emparelhamento.
7. **Ciclo euleriano**
   - Encontra um ciclo euleriano no multigrafo.
8. **Ciclo hamiltoniano**
   - Constrói o ciclo hamiltoniano a partir do ciclo euleriano.
9. **Cálculo da razão entre o ciclo hamiltoniano e a AGM**
   - Verifica se a solução está dentro da cota de 1.5×ótimo (Christofides).

## Saída Esperada

O programa exibe no terminal:
- Matriz de adjacência (original e corrigida)
- AGM e seu peso
- Vértices de grau ímpar
- Emparelhamento perfeito mínimo
- Multigrafo (AGM + emparelhamento)
- Ciclo euleriano
- Ciclo hamiltoniano
- Razão entre ciclo hamiltoniano e AGM
- Indicação se está dentro da cota de 1.5×ótimo

---

**Dúvidas ou problemas?**
Entre em contato com o(s) autor(es) ou consulte o professor da disciplina.
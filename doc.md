# Título sei la oq papapa
## Felipe e cecília q feiz

## 1. Introdução

Esse trabalho busca estudar paradigmas para solucionar problemas NP-Difíceis.

O problema alvo desse trabalho é o Caixeiro Viajante Geométrico. O problema do Caixeiro Viajante genérico consiste em encontrar um circuito hamiltoniano mínimo em um grafo completo, ou seja, buscar o menor caminho (em relação ao peso das arestas) que passe por todos os vértices do grafo e retorne ao ponto inicial. A condição de Geométrico adicionada ao problema consiste em afirmar que todos os pontos estão num mesmo plano 2D, assim os pesos do grafo são uma métrica.
( explicar métrica )
Essas condições são importantes para garantir o grau de aproximação dos algoritmos aproximativos, será abordada na seção 2.

Dentro desse contexto, analisaremos soluções de *backtracking* e algoritmos aproximativos para solucionar o problema do Caixeiro Viajante Geométrico.

## 2. Algoritmos

No desenvolvimento do trabalho foram implementados os algoritmos aproximativos *Twice-around-the-tree* (TaT) e o algoritmo de *Christofides*. Mais informações quanto a funcionamento e grau de aproximação destes serão dispostas a seguir.

### 2.1 Twice-around-the-tree

O algoritmo consiste em adquirir a árvore geradora mínima do grafo alvo. Depois, é contruído um multigrafo duplicando toda aresta da árvore geradora mínima. Nesse multigrafo, é buscado por um circuito euleriano qualquer (passe por todas as arestas). Por fim, são removidos os acessos a vértices repetidos no circuito, assim gerando um circuito hamiltoniano do grafo original.

Demonstração 2-Aproximativo

### 2.2 Christofides

Demonstração 1.5 Aproximativo



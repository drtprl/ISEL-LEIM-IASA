from .procura_melhor_prim import ProcuraMelhorPrim
from .aval.avaliador_custo_unif import AvaliadorCustoUnif
class ProcuraCustoUnif(ProcuraMelhorPrim):
    """A procura de custo uniforme é um caso particular da procura do 
    melhor-primeiro em que, utilizando a função de avaliação de uniforme, 
    colocando os nós na fronteira por ordem crescente segundo o custo acumulado
    até o nó.

    Neste caso, não é utilizada heurística, mas sim o custo dos nós explorados
    para calcular a saida da função f(n). Este ainda é um método de 
    procura não informada e não faz uso do conhecimento do domínio do 
    problema para ordenar a fronteira, simplesmente calcula os custo e, só
    depois, é que coloca na fronteira os nós.

    A procura não guiado exige exige ao algoritmo um exploração exaustiva em
    todo o espaço de estados até encontrar uma solução.
    
    Este algoritmo é óptimo e completo, porem face a complexidade computacional 
    temos um crescimento exponencial similar a procura em largura. Dependendo
    número de nós a expandir para encontrar uma solução este parâmetro pode
    variar.
    """
    
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())
from abc import ABC, abstractmethod

class Heuristica(ABC):
    """A classe heurística vai definir a função heurística h(n) da função f(n)
    na implementação do método h. Nos métodos de procura informada usamos uma
    heurística, que é definida em ciéncias como a busca de uma solução de um 
    problema perante métodos não exaustivo ao contrario dos métodos de procura
    não informada que realizam uma exploração exaustiva do espaço de estados.

    Está formula estima o custo do percurso de n até o objectivo, que podera 
    não corresponder ao valor real. Para uma herística ser óptima esta deve ser
    admissível, isto é que deve ser optimista, a estimativa do custo é sempre
    menor ou igual ao custo efectivo mínimo. 
    
    Como exemplo podemos usar a distância euclidiana como heurística, a linha 
    reta até ao objectivo vai ser sempre menor (nem sequer igual, mas sim a 
    menor) que o percurso real até ao objectivo, concluindo que está heurística
    é admissível. No lado contrario podemos usar o exemplo da distância de 
    Manhattan que só é admissível se o agente não poder realizar movimentos em 
    diagonal.

    Para poder definir uma heurística admissível devemos remover as restrições 
    do problema, no nosso projeto, geralmente é calcular a distância entre
    o nó corrente e o objectivo sem ter em conta os obstâculos ou, no caso da
    distância ser euclidiana, remover também a restrição de movimentos em 
    diagonal, pois o agente só se movimenta no eixo vertical e horizontal.
    """
    @abstractmethod
    def h(self, estado):
        '''
        Função heurística baseada na estimativa do custo.
        Exemplo: distância euclidiana do estado atual ao objectivo.
        '''
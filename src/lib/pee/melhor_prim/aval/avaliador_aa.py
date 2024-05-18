from .avaliador_heur import AvaliadorHeur

class AvaliadorAA(AvaliadorHeur):
    """Classe que implementa a f(n)=g(n)+h(n) da procura AA que é a combinação 
    do caminho já percorrido até ao nó, mais o custo estimado até ao objectivo.

    Esta classificação dos nós permite diminuir a complexidade espacial em 
    comparação com a procura de custo uniforme, porem terá sempre um custo 
    computacional maior que a procura sôfrega pois devem ser guardados os nós
    anteriores explorados para a comparação de caminhos, por isso dizemos que
    a procura AA é tem uma heurística consistente(monótona).

    Uma heurística admissível pode não ser consistente, para ser admissível 
    deve ser h(n)<= C* (C* - custo da solução óptima)
    """

    def prioridade(self, no):
        """Método calcula a f(n) que é a prioridade do nó.

        Args:
            no (No): Nó a expandir

        Returns:
            double: valor da função f(n)
        """
        return no.custo + self._heuristica.h(no.estado)
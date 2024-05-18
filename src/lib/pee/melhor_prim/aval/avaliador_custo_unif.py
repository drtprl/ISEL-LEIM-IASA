from .avaliador import Avaliador

class AvaliadorCustoUnif(Avaliador):
    """O avaliador de custo uniforme calcula a função de prioridade do nó sobre
    o custo acumulado até ao nó corrente.
    """

    def prioridade(self, no):
        return no.custo

    
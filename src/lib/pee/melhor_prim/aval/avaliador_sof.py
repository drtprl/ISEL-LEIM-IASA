from .avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    """O avaliador sôfrego implementa a função h(n) do mecanismo de procura
    sôfrega para calcular a prioridade do nó na fronteira de exploração
    segundo o valor do estado do no.
    """

    def prioridade(self, no):
        "f(n)=h(n) calculo da estimativa do nó corrente até o nó objectivo."
        return self._heuristica.h(no.estado)
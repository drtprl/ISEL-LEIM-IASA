from .aval.avaliador_sof import AvaliadorSof
from .procura_informada import ProcuraInformada

class ProcuraSofrega(ProcuraInformada):
    """A procura sôfrega é um método de procura informada pois utiliza o 
    conhecimento sobre o dominio do problema sem fazer uma busca exaustiva. 
    Esta solução pode ser mais prática que a procura A* pois não é consistente,
    não guardamos varios caminhos ótimos para posterior comparação, refletido
    na função f(n)=h(n) que como se pode ver é sub-óptima pois não faz uso do
    custo até ao nó atual para avaliar(calcular) a prioridade do nó corrente.
    """

    def __init__(self):
        super().__init__(AvaliadorSof())

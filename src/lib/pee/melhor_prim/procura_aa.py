from .procura_informada import ProcuraInformada
from .aval.avaliador_aa import AvaliadorAA
class ProcuraAA(ProcuraInformada):
    """A procura A* deve é uma procura informada, este método é o algoritmo que
    expande menos nós, mantendo as características de ser óptimo e completo,
    excepto nas situações de escolha entre nós com f(n) = C* (custo otimo até
    o nó objectivo). A complexidade computacional é exponencial e pode não ser
    a solução mais prática para resolver problema complexos.

    Para implementar a função f(n)=g(n)+h(n)(custo do inicio ao nó corrente +
    estimativa do nó corrente até o objectivo) devemos instanciar uma 
    heurística com a classe AvaliadorAA. Este é o calculo para posterior 
    rdenação da nossa fronteira de exploração.
    """

    def __init__(self):
        super().__init__(AvaliadorAA())
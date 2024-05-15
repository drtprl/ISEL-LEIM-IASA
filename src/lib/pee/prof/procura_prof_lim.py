from .procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    '''
    Diferenciamos esta procura em profundidade porque tem um
    limite e assim evitamos ocupar memoria a mais.
    '''

    @property
    def prof_max(self):
        return self.__prof_max
    @prof_max.setter
    def prof_max(self, valor):
        self.__prof_max  = valor

    def __init__(self, prof_max):
        self.__prof_max = prof_max
        super().__init__()

    def _expandir(self, problema, no):
        '''
        Este método serve para implementar do algoritmo da fronteira FIFO no caso
        que a profundidade do nó seja menor que a profunidade máxima permitida.
        '''
        return super()._expandir(problema, no) if no.profundidade < self.__prof_max else []
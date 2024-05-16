from .procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):
    """A classe ProcuraProfLim procura resolver um dos problemas da procura em 
    profundidade a grande ocupação de memoria ou busca infinita. Colocando um 
    limite na profundidade antes de realizar um "backtrack". 

    Exemplo: 

    Args:
        ProcuraProfundidade (_type_): _description_

    Returns:
        _type_: _description_
    """
    '''
    Diferenciamos esta procura em  porque tem um limite e assim evitamos ocupar
    memoria a mais.
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
        Este método serve para implementar do algoritmo da fronteira FIFO no 
        caso que a profundidade do nó seja menor que a profunidade máxima 
        permitida.
        '''
        return super()._expandir(problema, no) if no.profundidade < \
                                                self.__prof_max else []
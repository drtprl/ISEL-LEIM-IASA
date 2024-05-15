from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    '''
    
    '''
    def __init__(self):
        '''
        '''
        super().__init__(FronteiraLIFO())

    def _memorizar(self, no):
        '''
        
        '''
        self._fronteira.inserir(no)
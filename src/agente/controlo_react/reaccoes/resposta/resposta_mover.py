from ecr.resposta import Resposta
from sae import Accao

class RespostaMover(Resposta):
    '''
    
    '''
    def __init__(self, direccao):
        '''
        Resposta cuja ação é uma ação de movimentação
        indicada no argumento.
        '''
        super().__init__(Accao(direccao))
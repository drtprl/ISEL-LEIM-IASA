from ecr.reaccao import Reaccao
from .estimulo_obst import EstimuloObst


class EvitarDir(Reaccao):
    '''
    Classe que implementa a Reaccao.
    '''
    
    def __init__(self, direccao, resposta):
        estimulo = EstimuloObst(direccao)
        super().__init__(estimulo, resposta)
    
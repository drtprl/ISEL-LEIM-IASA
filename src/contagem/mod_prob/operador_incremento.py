from mod.operador import Operador
from .estado_contagem import EstadoContagem

class OperadorIncremento(Operador):

    @property
    def incremento(self):
        return self.__incremento

    def __init__(self, incremento):
        self.__incremento = incremento

    def aplicar(self, estado):
        '''
        Novo estado pelo significado do estado
        '''
        return EstadoContagem(estado.valor + self.__incremento)
    
    def custo(self, estado, estado_suc):
        '''
        Nesta implementação não é necessario os estado para o calculo
        do custo.
        '''
        return self.__incremento**2
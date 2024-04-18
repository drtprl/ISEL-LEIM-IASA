from abc import ABC, abstractmethod
class Problema(ABC):
    '''
    Problema, 
    '''

    @property
    def estado_inicial(self):
        return self.__estado_inicial
    @property
    def operadores(self):
        return self.__operadores
    
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        self.__operadores = operadores

    @abstractmethod
    def objectivo(self, estado):
        '''
        '''
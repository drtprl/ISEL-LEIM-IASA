from abc import ABC, abstractmethod
class Fronteira(ABC):
    '''
    '''
    @property
    def vazia(self):
        return len(self._nos) == 0

    def __init__(self):
        # Não fazemos uma variavel per se
        # mas sim uma propriedade que será calculada dinámicamente
        # para averiguar o tamanho do array de nos.
        # self.__vazia = False
        self.iniciar()
    
    def iniciar(self):
        self._nos = []
    
    @abstractmethod
    def inserir(self, no):
        '''
        '''

    def remover(self):
        return self._nos.pop(0)
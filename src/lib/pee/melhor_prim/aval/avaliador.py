from abc import ABC, abstractmethod
class Avaliador(ABC):
    '''
    Esta classe é equivalente a função f(n) para avaliação
    do custo de cada nó gerado.
    '''
    @abstractmethod
    def prioridade(self, no):
        '''
        
        '''
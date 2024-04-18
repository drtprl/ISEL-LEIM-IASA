from abc import ABC, abstractmethod
class Operador(ABC):
    '''
    Classe Operador representa as varias ações que provocam
    uma mudança de uma transição de estado.
    '''
    
    @abstractmethod
    def aplicar(self, estado):
        '''

        '''
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        '''
        Método que calcula o gasto realizado para transicionar
        entre o estado atual e sucessor.
        '''
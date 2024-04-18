from abc import ABC, abstractmethod
class Estado(ABC):
    '''
    Classe Estado representa com um identificador único 
    um objeto dentro do espaço de estados.
    '''

    @abstractmethod
    def id_valor():
        '''
        Método a implementar que segundo o tipo de criterio a escolher para
        a identificação única do Estado.
        '''
    
    def __hash__(self):
        return self.id_valor()
    
    def __eq__(self, other):
        '''
        Método gerado para comparar as identificações das instancias 
        de uma determinada classe.
        '''
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()

from abc import abstractmethod
from .comportamento import Comportamento

class ComportComp(Comportamento):
    """
    Classe que agrega conjuntos de comportamentos e requer de um
    método de selecção de acção para determinar a acção a realizar
    em função das respostas dos varios comportamentos internos.
    Um comportamento composto integra varias reações e cada uma 
    deve estar associada a uma ação. Posteriormente, são utilizados
    mecanismos de combinação e seleção de acções. 
    Modulo ecr: esquemas comportamentais reativos
    """
    def __init__(self, comportamentos):
        """
        Construtor
        """
        self.__comportamentos = comportamentos

    def activar(self, percepcao):
        """
        
        """
        accoes = []
        for comportamento in self.__comportamentos:
            accao = comportamento.activar(percepcao)
            if accao:
                accoes.append(accao)
        if accoes:
            return self.seleccionar_accao(accoes)
    
    @abstractmethod
    def seleccionar_accao(self, accoes):
        """
        """    
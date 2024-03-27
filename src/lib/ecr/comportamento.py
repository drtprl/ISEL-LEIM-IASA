from abc import ABC, abstractmethod

class Comportamento(ABC):
    """
    Classe que define um comportamento simples que é um conjunto
    de reações relacionadas entre si para evitar um obstáculo, conseguindo
    relacionar padrões de percepção com padrões de acção.
    Modulo ecr: esquemas comportamentais reativos
    """
    @abstractmethod
    def activar(self, percepcao):
        """
        
        """
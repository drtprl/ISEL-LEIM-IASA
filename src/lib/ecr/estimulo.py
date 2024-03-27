from abc import ABC, abstractmethod

class Estimulo(ABC):
    """
    Elemento que define a informação ativadora de uma reação
    para despertar um estimulo presente numa percepção,
    necessario para fazer associação estímulo/resposta.
    Modulo ecr: esquemas comportamentais reativos
    """
    @abstractmethod
    def detectar(self, percepcao):
        """Detetar estímulo"""
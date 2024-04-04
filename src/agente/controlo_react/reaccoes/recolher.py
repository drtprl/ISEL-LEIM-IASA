

from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.explorar.explorar_rodar import ExplorarRodar
from ecr.hierarquia import Hierarquia
class Recolher(Hierarquia):
    '''
    O comportamento recolher após a definição de objectivos e comportamentos,
    definimos os niveis de competencia segundo Hierarquía.
    '''
    # Equivalente a static de Java
    #__comportamentos = [AproximarAlvo(), EvitarObst(), Explorar()]
    __comportamentos = [AproximarAlvo(), Explorar()]
    def __init__(self):
        super().__init__(self.__comportamentos)
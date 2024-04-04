from .resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae import Direccao
from .evitar_dir import EvitarDir


class EvitarObst(Hierarquia):
    '''
    Esta classe implementa a arquitetura de subcção de Brooks,
    niveis de competência para concretizar o objetivo do agente.
    '''
    def __init__(self):
        # Resposta comum a todos os EvitarDir
        self.__resposta = RespostaEvitar()
        super().__init__(
            [EvitarDir(direccao, self.__resposta) for direccao in Direccao]
        )
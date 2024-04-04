from .estimulo_alvo import EstimuloAlvo
from ..resposta.resposta_mover import RespostaMover
from ecr.reaccao import Reaccao

class AproximarDir(Reaccao):

    def __init__(self, direccao):
        estimulo = EstimuloAlvo(direccao)
        resposta = RespostaMover(direccao)
        super().__init__(estimulo, resposta)


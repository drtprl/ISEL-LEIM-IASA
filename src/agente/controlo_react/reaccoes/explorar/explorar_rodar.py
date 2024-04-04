from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento
from sae import Direccao

class ExplorarRodar(Comportamento):
    __direccoes_rodar = {
            Direccao.NORTE: Direccao.ESTE,
            Direccao.ESTE: Direccao.SUL,
            Direccao.SUL: Direccao.OESTE,
            Direccao.OESTE: Direccao.NORTE}
    def activar(self, percepcao):
        direccao = self.__direccoes_rodar.get(percepcao.direccao)
        resposta = RespostaMover(direccao)
        accao = resposta.activar(resposta)
        return accao

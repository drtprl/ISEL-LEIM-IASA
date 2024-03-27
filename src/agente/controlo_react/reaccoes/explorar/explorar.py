from agente.controlo_react.reaccoes.resposta.resposta_mover_aleatoria import RespostaMoverAleatoria
from ecr.comportamento import Comportamento
class Explorar(Comportamento):
    '''
    Este comportamento realiza o contrato de Comportamento.
    '''
    def activar(self, percepcao):
        resposta = RespostaMoverAleatoria()
        accao = resposta.activar(percepcao)
        return accao
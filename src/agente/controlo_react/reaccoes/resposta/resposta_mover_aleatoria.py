from random import choice
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae import Direccao


class RespostaMoverAleatoria(RespostaMover):
    '''
    Resposta que é uma RespostaMover, esta passa uma direccao aleatoria
    para o construtor de RespostaMover que instancia uma Accao com a 
    Direccao aleatoria gerada nesta classe de teste.
    '''
    def __init__(self):
        direccao_aleatoria = choice(list(Direccao))
        super().__init__(direccao_aleatoria)
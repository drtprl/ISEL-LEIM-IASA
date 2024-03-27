from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae import Direccao

class AproximarAlvo(Prioridade):
    '''
    Aproximar alvo herda de prioridade, comportamento composto.
    Definimos um dos sub-comportamentos de Recolher. 
    Aproximar alvo instancia AproximarDir com cada uma das direccoes colocando
    uma prioridade a cada direccao e poder escolher a melhor direccao.
    A intensidade do estímulo é a distância ao alvo.
    '''
    def __init__(self):
        super().__init__([AproximarDir(direccao) for direccao in list(Direccao)])
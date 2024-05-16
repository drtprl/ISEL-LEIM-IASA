from mod.estado import Estado

class EstadoAgente(Estado):
    '''O estado do agente para os agentes deliberativos será
    um tuplo com coordenadas x e y.'''

    @property
    def posicao(self):
        return self.__posicao

    def __init__(self, posicao):
        self.__posicao = posicao

    def id_valor(self):
        '''Valor baseado no valor do estado'''
        return hash(self.__posicao)
from mod.operador import Operador
from sae import Accao
import math
from .estado_agente import EstadoAgente

class OperadorMover(Operador):

    @property
    def ang(self):
        """Retornamos o valor da direccao que é um angulo em si mesmo"""
        return self.__accao.direccao.value
    
    @property
    def accao(self):
        return self.__accao

    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__accao = Accao(direccao)

    def __translacao(self, posicao, distancia, angulo):
        '''Método coeso, modularidade.
        coeso é que ao modularizar devemos juntar
        as coisas segundo partilhem coisas'''
        x, y = posicao
        dx = round(distancia*math.cos(angulo))
        dy = -round(distancia*math.sin(angulo))
        nova_posicao = x + dx, y + dy
        return nova_posicao
    
    def aplicar(self, estado):
        '''
        Este método server para aplicar a distancia do passo e analizar se
        essa translacao é um estado válido dentro dos estados guardados no
        nosso modelo do mundo
        '''
        #tava escrito translaccao
        nova_posicao = self.__translacao(estado.posicao, self.accao.passo, self.ang)
        novo_estado = EstadoAgente(nova_posicao)
        # Só devolvemos o estado se ele não for um obstáculo,
        # nesse caso deve estar no estados validos do modelo do mundo.
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado 
    
    def custo(self, estado, estado_suc):
        '''
        O custo sera a distancia euclidiana sobre dois pontos do modelo
        '''
        return math.dist(estado.posicao, estado_suc.posicao)
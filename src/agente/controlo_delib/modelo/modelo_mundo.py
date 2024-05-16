import math
from .estado_agente import EstadoAgente
from plan.modelo.modelo_plan import ModeloPlan
from sae import Direccao, Elemento
from .operador_mover import OperadorMover

class ModeloMundo(ModeloPlan):

    @property
    def alterado(self):
        '''
        Indica se foi alterado de algum dos parâmetros
        do modelo do mundo para a posterior deliberação do agente.
        O mundo é  alterado se foi recolhido um alvo'''
        return self.__recolha
    
    @property
    def elementos(self):
        return self.__elementos 

    def __init__(self):
        self.__posicao = None
        self.__elementos = {}
        self.__recolha = False
        self.__estados = []
        self.__estado = None
        self.__operadores = [OperadorMover(self,direccao)for direccao in\
                                           Direccao]
        self.__alterado = False
    
    def obter_estado(self):
        return self.__estado
    
    def obter_estados(self):
        return self.__estados
    
    def obter_operadores(self):
        return self.__operadores
    
    def obter_elemento(self, estado):
        #fazer con getter() para evitar exeção
        return self.__elementos.get(estado.posicao)
    
    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)
    
    def actualizar(self, percepcao):
        '''
        Os métodos todos são atualizados com a percepcao que tem a 
        informação nos seus atributos sobre a posicao do agente, posicoes
        validas em posicoes, recolha indica se recolheu um alvo ou se colidio
        com colisao. 
        '''
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__estados = [EstadoAgente(posicao) for posicao in \
                           percepcao.posicoes]
        self.__elementos = percepcao.elementos
        # recolha, vem de sae e indica se recolheu um alvo
        self.__recolha = percepcao.recolha
    
    def mostrar(self, vista):
        """usamos o método items() para devolver tuplos com (key, value)"""
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
            vista.marcar_posicao(self.__estado.posicao)
from sae import Controlo
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from .mec_delib import MecDelib

class ControloDelib(Controlo):

    def __init__(self, planeador):
        self.__planeador = planeador
        self.__plano = None
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objectivos = None
    
    def processar(self, percepcao):
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        self.__mostrar()
        return self.__executar()
    
    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)
    
    def __reconsiderar(self):
        if not self.__plano or self.__modelo_mundo.alterado:
            return True 

    def __deliberar(self):
        self.__objectivos = self.__mec_delib.deliberar()
    
    def __planear(self):
        self.__plano = self.__planeador.planear(self.__modelo_mundo,\
                                                self.__objectivos)
    
    def __executar(self):
        if self.__plano:
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)
            if operador:
                return operador.accao
            else:
                self.__plano = None
            
    def __mostrar(self):
        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)
        if self.__plano:
            self.__plano.mostrar(self.vista)
        if self.__objectivos:
            for objectivo in self.__objectivos:
                self.vista.marcar_posicao(objectivo.posicao)


from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from sae import Elemento
#from modelo.estado_agente import EstadoAgente

class MecDelib:

    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
    
    def deliberar(self):
        """Fins a atingir no modo de estado
        os alvos são os objectivos"""
        estados = self.__modelo_mundo.obter_estados()
        alvos = [estado for estado in estados if \
                 self.__modelo_mundo.obter_elemento(estado) \
                == Elemento.ALVO]
        if alvos:
            alvos.sort(key=self.__modelo_mundo.distancia)
            return alvos
        

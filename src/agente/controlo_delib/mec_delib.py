from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from sae import Elemento
#from modelo.estado_agente import EstadoAgente

class MecDelib:
    """O mecanismo de deliberação fornece o mecanismo deliberativo do nosso 
    agente. Este será invocado cada vez que o modelo do mundo percepcione
    uma alteração do ambiente com a finalidade de encontrar os elementos alvo,
    ordenando eles na lista de alvos por ordem de distancia ao agente. O 
    cálculo realizado é a distância euclidiana.
    """
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
        

from plan.planeador import Planeador

class PlaneadorPDM(Planeador):

    @property
    def gama(self):
        return self.__gama
    @property
    def delta_max(self):
        return self.__delta_max

    def __init__(self, gama = 0.85, delta_max = 1.0):
        self.__gama = gama
        self.__delta_max = delta_max
    
    def planear(self, modelo_plan, objectivos):
        raise NotImplementedError
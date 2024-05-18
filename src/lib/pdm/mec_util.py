

class MecUtil:

    @property
    def gama(self):
        return self.__gama
    
    @property
    def delta_max(self):
        return self.__delta_max

    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
    
    def utilidade(self):
        """Self-made"""
        U = {}
        while(delta < self.delta_max):
            Uant = U.copy.deepcopy()
            delta = 0
            for estado in self.__modelo.obter_estados():
                U[estado] = self.util_accao(estado, self.__modelo.A(estado),\
                                             Uant)
        return U


    def util_accao(self, s, a, U):
        raise NotImplementedError
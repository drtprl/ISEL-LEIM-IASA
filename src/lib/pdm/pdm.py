from .mec_util import MecUtil

class PDM:

    def __init__(self, modelo, gama, delta_max):
        self.__mec_util = MecUtil(modelo, gama, delta_max)
        self.__modelo = modelo
    
    def politica(self, U):
        #guardamos funções e não valores
        S, A = self.__modelo.S, self.__modelo.A
        pol = {}
        for s in S():
            if A(s):
                # arg max accao que maximiza
                pol[s] = max(A(s),\
                             key=lambda a: self.__mec_util.util_accao(s,a,U))
        return pol
    
    def resolver(self):
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U, pol
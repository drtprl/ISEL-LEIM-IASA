import copy

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
        """A utilidade devolve um dicionario onde a chave é o proprio estado
        e o valor é a utilidade do estado. Servira mais adiante para calcular
        """
        S, A = self.__modelo.S, self.__modelo.A
        U = {s:0 for s in self.__modelo.S}
        while(delta > self.delta_max):
            Uant = copy.deepcopy(U)
            delta = 0.0
            for s in S:
                U[s] = self.util_accao(s, A(s), Uant)
                delta = max(delta, abs(U[s]-Uant[s]))
        return U


    def util_accao(self, s, a, U):
        """Utilidade de cada ação é calculada tendo """
        T, R = self.__modelo.T, self.__modelo.R
        sucs = self.__modelo.suc(s,a)
        Ua = sum(T(s,a,suc)*(R(s,a,suc)+(self.gama*U[suc])) for suc in sucs)
        return Ua
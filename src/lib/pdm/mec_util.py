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
        e o valor é a utilidade do estado.
        O algoritmo tem o seguinte ciclo:
            1. Colocar todos os estados com utilidade 0.0
            2. Entrar num ciclo que busca maximizar a utilidade
            3. fazer uma copia da utilidade para poder fazer uma comparação
            4. Cálcular a utilidade da acção 
                4.1. Calcular a probabilidade de transição
                4.2. Soma da Recompensa desta acção
                4.3. Utilidade da próxima acção
            5. Retornar a utilidade
        """
        S, A = self.__modelo.S, self.__modelo.A
        U = {s:0.0 for s in S()}
        while True:
            Uant = U.copy() # Shallow copy
            delta = 0 # Valor absoluto
            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)],\
                            default = 0)
                delta = max(delta, abs(U[s]-Uant[s]))
            if delta <= self.__delta_max:
                break
        return U


    def util_accao(self, s, a, U):
        """Utilidade de cada ação é calculada tendo """
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc 
        gama = self.__gama
        return sum(T(s,a,sn)*(R(s,a,sn)+gama*U[sn]) for sn in suc(s, a))
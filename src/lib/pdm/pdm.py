from .mec_util import MecUtil

class PDM:
    """A classe PDM, processos de decissão de Markov, 
    """
    def __init__(self, modelo, gama, delta_max):
        self.__mec_util = MecUtil(modelo, gama, delta_max)
        self.__modelo = modelo
    
    def politica(self, U):
        """A política deve representar o que o agente deve fazer para cada 
        estado. Por tanto, esta função devolve a accao recomendada pela 
        polític para este estado.

        Args:
            U (Utilidade): Para produzir uma política devemos ter a utilidade


        Returns:
            _type_: _description_
        """
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
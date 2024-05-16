from .procura_prof_lim import ProcuraProfLim

class ProcuraProfIter(ProcuraProfLim):
    """Este algoritmo de procura em profundidade busca a eficiencia de memoria 
    ao procurar a solução em cada um dos níveis da arvore de procura,
    aprofundando segundo um incremento estabelecido antes de atingir o limite
    de profundidade, nesse caso não existe solução ao nosso problema com este 
    algoritmo ou simplesmente não há solução.
    """

    def procurar(self, problema, inc_prof=1, limite_prof=100):
        for profundidade in range(0, limite_prof+1, inc_prof):
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao

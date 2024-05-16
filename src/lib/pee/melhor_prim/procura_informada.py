from .procura_melhor_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):

    def procurar(self, problema, heuristica):
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
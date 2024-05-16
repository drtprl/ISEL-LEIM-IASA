from .avaliador import Avaliador

class AvaliadorHeur(Avaliador):
    '''
    Esta classe especializa a interface Avaliador para poder colocar .
    '''
    def definir_heuristica(self, heuristica):
        self._heuristica = heuristica
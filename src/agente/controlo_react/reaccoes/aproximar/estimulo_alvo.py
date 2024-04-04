from ecr.estimulo import Estimulo
from sae import Elemento


class EstimuloAlvo(Estimulo):

    def __init__(self, direccao, gama = 0.9):
        self.__direccao = direccao
        self.__gama = gama # A base da potencia da intensidade

    def detectar(self, percepcao):
        elemento, distancia, _ = percepcao[self.__direccao]
        if elemento == Elemento.ALVO:
            intensidade = self.__gama**distancia #quanto menor a distancia, menor a gama
        else:
            intensidade = 0.0
        return intensidade
    


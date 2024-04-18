from ecr.estimulo import Estimulo

class EstimuloObst(Estimulo):

    def __init__(self, direccao, intensidade = 1.0):
        self.__intensidade = intensidade
        self.__direccao = direccao

    def detectar(self, percepcao):
        if(percepcao.contacto_obst(self.__direccao)):
            return self.__intensidade
        else:
            return 0.0
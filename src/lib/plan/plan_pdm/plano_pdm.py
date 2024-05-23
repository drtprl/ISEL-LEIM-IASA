from plan.plano import Plano

class PlanoPDM(Plano):

    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica
    
    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
    
    def mostrar(self, vista):
        print(self.__utilidade)
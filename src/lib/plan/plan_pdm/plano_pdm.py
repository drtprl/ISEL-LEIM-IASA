from plan.plano import Plano

class PlanoPDM(Plano):

    @property
    def politica(self):
        return self.__politica
    @property
    def utilidade(self):
        return self.__utilidade

    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica
    
    def obter_accao(self, estado):
        raise NotImplementedError
    
    def mostrar(self, vista):
        raise NotImplementedError
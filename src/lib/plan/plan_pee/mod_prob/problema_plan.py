from mod.problema import Problema

class ProblemaPlan(Problema):

    def __init__(self, modelo_plan, estado_final):
        self.__estado_final = estado_final
        super().__init__(modelo_plan.obter_estado(), \
                         modelo_plan.obter_operadores())

    def objectivo(self, estado):
        return self.__estado_final == estado

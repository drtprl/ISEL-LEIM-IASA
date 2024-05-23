from plan.planeador import Planeador
from pdm.pdm import PDM
from pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM

class PlaneadorPDM(Planeador):
    """Precisa de ser compativel com Planeador e PDM"""

    def __init__(self, gama = 0.85, delta_max = 1.0):
        self.__gama = gama # depende do gama 
        self.__delta_max = delta_max
    
    def planear(self, modelo_plan, objectivos):
        if objectivos:
            modelo_pdm = ModeloPDMPlan(modelo_plan, objectivos)
            pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
            utilidade, politica = pdm.resolver()

            return PlanoPDM(utilidade, politica)
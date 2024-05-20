from plan.modelo.modelo_plan import ModeloPlan
from .modelo_pdm import ModeloPDM

class ModeloPDMPlan(ModeloPDM):
    """
    """
    @property
    def rmax(self):
        return self.__rmax
    
    @property
    def objectivos(self):
        return self.__objectivos
    
    @property
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
    
    @property
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    @property
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()


    def __init__(self, modelo_plan, objectivos, rmax = 1000.0):
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax

    def S(self):
        self.obter_estados()
    
    def A(self, s):
        ''''''
        raise NotImplementedError

    def T(self, s, a, sn):
        ''''''
        raise NotImplementedError

    def R(self, s, a, sn):
        ''''''
        raise NotImplementedError
        
    def suc(self, s, a):
        ''''''
        raise NotImplementedError

    


